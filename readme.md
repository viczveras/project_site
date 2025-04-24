


          
# BluePost

## 📝 Descrição
BluePost é uma plataforma de compartilhamento de imagens desenvolvida com Flask, permitindo que usuários criem contas, façam login e compartilhem suas fotos em um ambiente moderno e intuitivo.

## 🚀 Funcionalidades
- Sistema de autenticação completo (login/registro)
- Upload e visualização de imagens
- Perfil de usuário personalizado
- Visualização de imagens em modal
- Design responsivo
- Interface moderna e intuitiva

## 🛠️ Tecnologias Utilizadas
- **Backend**: Python/Flask
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: SQLite
- **Bibliotecas**:
  - Flask-SQLAlchemy
  - Flask-Login
  - Flask-WTF
  - Flask-Bcrypt
  - Werkzeug

## 🎨 Design
- Paleta de cores 60-30-10
  - Cor primária: #f8f9fa (60%)
  - Cor secundária: #e9ecef (30%)
  - Cor destaque: #4a90e2 (10%)
- Fontes: Poppins e Montserrat
- Design responsivo para diferentes tamanhos de tela

## 💻 Requisitos
- Python 3.x
- pip (gerenciador de pacotes Python)

## 🔧 Instalação
1. Clone o repositório
```bash
git clone https://seu-repositorio/BluePost.git
cd BluePost
```

2. Crie e ative um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados
```bash
python criar_db.py
```

5. Execute a aplicação
```bash
python main.py
```

## 📁 Estrutura do Projeto
```
BluePost/
├── static/
│   ├── css/
│   │   └── style.css
│   └── fotos_posts/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── criarconta.html
│   └── perfil.html
├── __init__.py
├── forms.py
├── models.py
├── routes.py
├── criar_db.py
└── main.py
```

## 🔐 Segurança
- Senhas criptografadas com Bcrypt
- Proteção contra CSRF
- Validação de formulários
- Nomes de arquivos seguros
- Autenticação de usuário

## 🌟 Características do Sistema
- **Sistema de Login**: Autenticação completa com email e senha
- **Cadastro de Usuário**: Registro com validação de dados
- **Upload de Fotos**: Sistema seguro de upload de imagens
- **Perfil Personalizado**: Cada usuário tem seu próprio espaço
- **Visualização de Imagens**: Modal interativo para visualização de fotos

## 🤝 Contribuição
Para contribuir com o projeto:
1. Faça um Fork
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ⚠️ Importante
- Mantenha as chaves secretas em variáveis de ambiente
- Não compartilhe informações sensíveis
- Faça backup regular do banco de dados
- Mantenha as dependências atualizadas

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📧 Contato
Para questões e sugestões, por favor abra uma issue no repositório do projeto.

        