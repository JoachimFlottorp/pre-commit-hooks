# Pre Commit Hooks

## Hooks Available

#### `go-run-test`

Run the built in go test command

- Will print out the name of the failed test

#### `go-run-fmt`

Run the built in gofmt command

- Defaults to failing if the formatter complains
- Allows for automatically formatting with `args: ['--auto']`
