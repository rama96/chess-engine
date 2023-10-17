# chess-engine

Building Chess Engines for Fun


### [Adding env variables](https://github.com/rama96/animals_prediction#adding-env-variables)

Create a .env file and add your python path and Microsoft azure_key to the same . Run the below commands to add get your .env added to your environment

```shell
printf "\n# Adding this command to read local .env file" >> env/bin/activate 
printf "\nexport $(grep -v '^#' .env | xargs)" >> env/bin/activate
```
