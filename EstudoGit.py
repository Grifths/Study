#git status é comando para ve se o comando está no portifolio. Pois só estándo no portifolio q ele pode ser salva

print("Olá mundo") #Se aparecer Untracked files signfinca q não está no git
print("Aprendendo git! Usando o git checkout -b para criar um novo branch ")

#Comando git add . para adicionar! Com o "." ele adiciona todos os arquivos, se não quiser é só colocar o nome do arquivo especifico
#git commit para comitar nosso código! E utiliza o -a(Adicionar todo tipo de arquivo ao commit) -m(Ele vc adiciona uma mensagem para alguém tenha um norte ao ver seu commit)
#Exemplo de como fica: git commit -a -m "Criando print olá mundo"

# digitando git branch conseguimos observar a lista de brach! Para poder acessalos e o que está em verde é oq eu estou

#git merge test. o merge é oq uni os códigos, como estou no main ele vai unir o "teste" e jogar para o main
#Só digitar git merge "nome do brench que deseja juntar"

# Dando o Git status novamente vc ve pela mensagem: "nothing to commit, working tree clean" que não tem nada para ser comitado
#Então é um bom ponto de finalização de tarefa pois as pendendencias com o git foi resolvida

#Para criar uma um git compartilhando para as pessoas utlizarem o projeto junto é necessario criar repositorio um no github

#Acessando o git e utilizando o git remote add origin "link" adiciona uma conexão ao pc e o repositorio do git
#git branch -M main! Estou dizendo que meu branch principal vai se chamar main! Agora ele vai parear os branch main de cada repositorio
#git push -u origin main. Este comando é para enviar nosso código para o repositorio que estamos conectado

#O ideal é cada desenvolver ter seu branch e depois unilos de forma coordernada! Pois são muitas pessoas trabalhando
#git chekout -b ! Aqui está criando um brench novo para fazer "MINHA PARTE"
# -b simboliza a criação de um novo branch

#git push --set-upstream origin teste ! Ele vai mandar para meu reposotorio só que um novo branch lá

print("Nova demanda")

#git pull é para puxar os projetos que estão no git hub para o nosso pc

#Para clonar projeto. Usado quando necessitamos pegar um projeto que já está sendo usado e precisamos dele
#para  clonar o projeto utiliza "git clone "url do projeto 'nome da pasta' " Mas o direcionamento continua igual
