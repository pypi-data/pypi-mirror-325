import os

_include_iteration_max_depth = 16

"""
Goal is to be able to run an 'eda' command, such as:
     > eda sim --target-packager <--stop-before-compile> \
               --tool verilator [--waves] [--dump-vcd] [other args] \
               <files or target>

Or a 'multi sim' command:
     > eda multi sim --target-packager <--stop-before-compile> \
               --tool verilator [--waves] [--dump-vcd] [other args] \
               <files or target wildcard>

And doing so would create:
   ./eda.work/<target>_sim/target_packager/
      ./DEPS.yml              -- new file with single target, all defines, incdirs, sources, top, etc.
      ./<all source files>    -- edited to flatten path information in `include
      ./<all `included files> -- edited to flatten path information in `include
      ./test.json             -- single file that can be as starting point for test runner service
                              -- Or a singular test.jsonl

A multi sim command would also create:
   ./eda.work/multi/tests.jsonl

And, we could re-run a single target in place as, but won't support this for 'multi sim':
  > cd ./eda.work/<target>_sim/target_packager/
  > eda sim test

**Note - we already have `eda export (target)` using class CommandExport. It does *some* of this
already, but is more tailored to putting files and a DEPS.yml in an output directory, and
does not take a simulation tool or other args. I'd really like to be able to spell out
what I want Frogger to run w/ all args and have that go in some 'test.json' that Frogger can
know about.

`include problem:
1. In SystemVerilog, a `include "foo.svh", no tools allow you to add this to your compile/build
   flow via filename. They all do this per directory.
   -- As a result, we do not track includes, other than "incdirs" in our DEPS.yml tables.
   -- relative path or absolute path includes are allowed:
      - `include "../../../../usr/bin/foo.svh"
      - `include "deeper/path/lets/go/foo.svh"
2. Given a compile, we do not know the exact individual files were `include'd.
3. Verific will not tell us which files wer actually `include'd in $root scope (would tell us
   within the module scope).
4. WHY IS THIS A PROBLEM
   - If we do nothing, Frogger will be responible for creating all relative or absolute
     directories. I see this as a security risk and infeasible to implement.
     -- aka, Frogger runs a test in /
5. Solutions:
   a. One option is: we make a decision to not support path information in includes, and
      manage this only in DEPS.yml 'incdirs'.
      -- This may not be ideal for some hypothetical customer in the future.
         (If you want to use our tool and Frogger, refactor your code first!)
   b. Another option is - we support limited parsing in this "eda sim --target-packager" flow
      to copy + edit the file to strip path information in includes, so that Frogger can create
      all files in a single working directory.


*IF* we make the decision to only support `include w/out path information in
the opencos repo, and suggest that this is preferred, then <all * files> could
instead be symbolic links.
   ./eda.work/<target>_sim/target_packager/
      ./DEPS.yml              -- new file with single target, all defines, incdirs, sources, top, etc.
      ./<all source files>    -- as symbolic links
      ./<all `included files> -- as symbolic links
      ./test.json             -- single file that can be as starting point for test runner service


*IF* we want to support relative or absolute path based `include "../../foo.svh", then
we get to unravel that with a copied and edited file.
Looking in eth-puzzles/bin/create_tests_jsonl_eda.py, the first step is running (since we didn't
edit eda.py at all) effectively:

     > eda sim --stop-before-compile --tool verilator <some-target>

and examining the eda.work/some-target_sim/compile_only.sh file.# From there,
the commands are split and we figure out incdirs, defines, source files, top
module name and any other knobs.
We then get the full path information of every source file, and infer the 'top'
file if it was not set otherwise. Finally, we resolve the `include nightmare in
all source files, and check that they exist in the incdirs we know about.

** If a file has no `include, and no edits, it will be a symbolic link
** If a file had any edits, it will not be a symbolic link
** We must check that edited files only have affected diff lines on lines containing `include.


An example packaged DEPS.yml file:

test:

  multi:
    ignore:
      # This is required so that generated DEPS.yml files are not picked
      # up by future 'eda multi sim' commands.
      - commands: sim synth build
  incdirs: .
  deps:
    - oclib_assert_pkg.sv
    - oclib_pkg.sv
    - oclib_memory_bist_pkg.sv
    - oclib_uart_pkg.sv
    - ocsim_pkg.sv
    - ocsim_packet_pkg.sv
    - ocsim_tb_control.sv
    - oclib_ram1rw.sv
    - oclib_ram1rw_test.sv
  top: oclib_ram1rw_test
  defines:
    LATENCY: 0


An example of a test.json file (w/out ## comments b/c json is a no comments zone):
{
  "name":    "oclib_ram1rw_test",  ## This might match the DEPS.yml - <target>: top value.
                                   ## Drew would expect this to be the how I can identify my test
                                   ## when I want to look a logs, errors, artifacts

  "eda":        {                  ## Table/dict entry with key "eda" indicates that
                                   ## this will be using 'eda' to run the test
    "command": "sim",              ## What is the eda command: sim, may support others eventually.
    "target": "test",              ## Name of the DEPS.yml <target>.
                                   ## Could instead use "tb_name" but this is Drew's preference.
    "args": [],                    ## Optional Args list, for example, ["--seed", "1"]
    "waves": true,
    "tool": "verilator"

  },
                                   ## Based on the above information, Frogger should be expected to run:
                                   ## > eda <command> <args> [--waves] --tool <tool> <target>

                                   ## If we find <args> to be gross or bad-security-practice
                                   ## then I'm not sure on the alterative. Frogger could
                                   ## be aware of allow-listed args that 'eda' suports, so
                                   ## Chip team putting its desired command in a json Array of
                                   ## args is not any different than a space separated string?
                                   ## recommand: mylist = shlex.split(eda_command)


  "files": [
    {"name": "DEPS.yml",          "content": <string file contents> },
    {"name": oclib_assert_pkg.sv, "content": <string file contents> },
    ## ...
    {"name": oclib_ram1rw_test.sv, "content": <string file contents> },

    ## Note that this will match the same order in the Array in DEPS.yml <target>:deps value.
    ## This is the compile order.

    ## We will not pass other hidden information that Frogger has to deal with. Any
    ## 'defines' or 'incdirs' or other Verilator compile flags will be in the DEPS.yml.
  ],

  ## AI Team may have other exciting test runner Table key/value items. Drew has no use for:
  ## - canonical_dut, dut, query, prefix, top, tb_name (if I get "eda_target")
}
"""


# TODO(drew): take class CommandExport, make these mostly helper style methods in something like
# export_helper.py that take a CommandDesign object handle, that way I can have CommandSim call the same
# junk if necessary when arg --target-export or --target-packager
