# Nav CLI

Nav CLI is a tool that allows to create command line interfaces that can be navegable through routes
The same way you define routes in an API, you define views in Nav CLI.

## Views

A View is an abstraction that contains a list of options that can be navegable and / or run a previously define procedure.

## Options
The options are structs with a label, an action and an optional redirect.
If a option doesn't define a redirect view, then when is selected, the actions will be executed and end the exeution of the app

## Highlights

A Hightlight allows you to visualize differently a focused options over the rest of them. You can define your own highlights but always following the structure define by the Base class