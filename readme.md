# pBrainfuck - Brainfuck interpreter on python

## BrainFuckInterpreter
### Fields
* `cells_number` - *integer*. default value: **30000**
* `memory` - *list of integer*. size = `cells_number`.
* `pointer` - *integer*. default value: **0**.
* `printEnd` - *string*. default value: `''`.
* `version` - *float*. determines version of Interpreter.
### Instructions
1. `+` - increment cell value in `memory`. the address will be a `pointer` value.
2. `-` - decrement cell value in `memory`. the address will be a `pointer` value.
3. `>` - increment `pointer` value.
4. `<` - decrement `pointer` value.
5. `.` - print cell value from `memory`. the address will be a `pointer` value.
6. `*` - print ascii character using cell value from `memory`. the address will be a `pointer` value.
7. `,` - scan integer value from keyboard and write it in cell from `memory`. the address will be a `pointer` value.
8. `[` - start loop. while cell value in `memory` on address `pointer` not equal 0, execute loop.
9. `]` - end loop.
### Methods
1. `process_cmd(cmd: str)` - execute `cmd` command
2. `start_loop(instructions: str, pointer_to_check: int = -1)` - start new loop and execute every cmd from `instructions` string. If `pointer_to_check` then execute all commands from `instructions` one time. Otherwise, execute commands, while value from `memory` cell on `pointer` address will not be equal 0.
3. `readfile(filename: str)` - read all instructions from `filename` file and call `start_loop`
4. `readline(line: str)` - call `start_loop`. `instructions = line`

## BFShell
### Fields
* `bfi` - `BrainFuckInterpreter` object
* `instr_stack` - *string*. stack of instructions that were inputed in shell and executed
* `version` - *float*. determines version of `BFShell`.
### Instructions
1. `/` - write `BFShell` commands list.
2. `|` - execute all code from `instr_stack`
3. `~` - run another interpreter and execute code from file
4. ` - clear instruction stack
5. `=` - quit