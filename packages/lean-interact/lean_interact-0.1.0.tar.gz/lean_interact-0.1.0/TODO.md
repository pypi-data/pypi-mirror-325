# TODO

- (hard) Handle timeout more properly, i.e. directly from within the Lean REPL
- Pre-compile binaries so that users don't have to compile them themselves
- Add example scripts
- Make sure that AutoLeanServer doesn't restart between running a command and storing it to the session cache
- Modify Lean REPL to not record environment/proof states
- Improve session cache performance
  - Currently it saves and reload every states independently, which might be slower thn replaying everything in the right dependency order
  - Before I was replaying from Python the commands keeping the sequential order. Maybe I should do that again
- Lean REPL doesn't validate proofs, so empty goal list does not mean the proof is valid
- Lean REPL: add option to get the initial proof state of each declaration in a code
- Add tests:
  - Check that we can't prove false
  - Check that pickling / unpickling doesn't change declaration type (def => noncomputable def)
- Capture interaction with REPL in dataclasses
