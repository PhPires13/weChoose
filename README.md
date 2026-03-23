# weChoose

## Roles
- Bárbara Diniz Abreu
    - Backend
- João Pedro Figueiredo Bicalho
    - Frontend
- Júlia Souza Moura
    - Frontend
- Pedro Henrique Gonçalves Pires
    - Backend

## Objetivo do Sistema

O sistema tem como objetivo gerenciar o saldo digital do restaurante universitário, permitindo que usuários recarreguem sua carteirinha presencialmente ou pelo site. Ao acessar o restaurante, basta utilizar a carteirinha na catraca para liberação rápida da entrada. A plataforma busca reduzir filas, otimizar o fluxo de atendimento e oferecer mais praticidade no pagamento das refeições. Além disso, possibilita o acompanhamento do saldo e histórico de recargas de forma simples e acessível.

## Tecnologias
<table style="border: none;">
    <tr>
        <td align="center">
            <h3>Backend</h3>
            <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="python" height="40"/> </a> <br>
            <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://static.djangoproject.com/img/logos/django-logo-negative.svg" alt="django" height="40"/> </a> <br>
            <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://www.django-rest-framework.org/img/logo-dark.png#only-dark" alt="django" height="40"/> </a> <br>
        </td>
        <td align="center">
            <h3>Frontend</h3>
            <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" height="40"/> </a>
            <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" height="40"/> </a>
            <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" height="40"/> </a> <br>
            <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://react.dev/images/brand/wordmark_dark.svg" alt="react" height="40"/> </a> <br>
            <a href="https://mui.com" target="_blank" rel="noreferrer"> <img src="https://cdn.cloudinary.com/stichting-frontend-amsterdam/image/upload/v1724858269/mui-logo-dark-text_qi0eho.png" alt="react" height="40"/> </a>
        </td>
    </tr>
    <tr>
        <td align="center">
            <h3>Database</h3>
            <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://brasilcloud.com.br/wp-content/uploads/2018/09/postgresql-logo1.png" alt="postgresql" height="40"/> </a>
        </td>
        <td align="center">
            <h3>DevOps</h3>
            <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img   src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Git-logo.svg/3840px-Git-logo.svg.png" alt="git" height="40"/> </a>
        </td>
    </tr>
</table>

## Histórias de Usuário

### 1. Recarga online

**Como** aluno
**Quero** recarregar o saldo da minha carteirinha pelo site
**Para** evitar filas e garantir crédito antes de chegar ao restaurante

---

### 2. Recarga presencial

**Como** aluno
**Quero** recarregar minha carteirinha no local de atendimento
**Para** conseguir adicionar saldo mesmo sem acesso ao site

---

### 3. Consulta de salso

**Como** aluno
**Quero** consultar meu saldo disponível
**Para** saber se tenho crédito suficiente para realizar uma refeição

---

### 4. Histórico de transações

**Como** aluno
**Quero** visualizar o histórico de recargas e utilizações
**Para** acompanhar meus gastos no restaurante

---

### 5. Validação na catraca

**Como** aluno
**Quero** passar minha carteirinha na catraca e ter o acesso liberado automaticamente
**Para** entrar rapidamente no restaurante sem precisar realizar pagamentos na hora

---

### 6. Leitura da carteirinha

**Como** operador de caixa
**Quero** ler a carteirinha do aluno no sistema
**Para** identificar o usuário e acessar suas informações de saldo

---

### 7. Processamento de recarga

**Como** operador de caixa
**Quero** registrar recargas presenciais no sistema
**Para** atualizar imediatamente o saldo do aluno

---

### 8. Confirmação de identidade

**Como** operador de caixa
**Quero** visualizar a foto do aluno ao passar a carteirinha
**Para** validar que a pessoa utilizando o cartão é o próprio titular e garantir a segurança do acesso

---

### 9. Controle de acesso

**Como** sistema
**Quero** validar automaticamente se o aluno possui saldo suficiente ao passar na catraca
**Para** liberar ou bloquear o acesso de forma rápida e sem intervenção manual
