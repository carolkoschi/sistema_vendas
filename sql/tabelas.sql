create table clientes(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    email varchar(150) unique not null,
    telefone varchar(20) not null,
    dataCadastro datetime not null default getdate()
);
GO
create table endereco(
    id int not null IDENTITY(1,1) primary key,
    logradouro varchar(255) not null,
    numero varchar(10) not null,
    complemento varchar(100) not null,
    bairro varchar(100) not null,
    cidade varchar(100) not null,
    estado varchar(50) not null,
    cep varchar(20) not null,
    pais varchar(50) not null,
);
GO
CREATE TABLE tipoEndereco(
    id int not null IDENTITY(1,1) primary key,
    nome VARCHAR(50) not null,
);
GO
create table clienteEndereco(
    id int not null IDENTITY(1,1) primary key,
    idCliente int not null,
    idEndereco int not null,
    idTipoEndereco int not null,
);
GO
create table produtos(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    preco decimal(15,4) not null,
    estoque int not null,
    idcategoria int not null,
);
GO
create table categoria(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
);
GO
create table pedidos(
    id int not null IDENTITY(1,1) primary key,
    idCliente int not null,
    IdFuncionario int not null,
    idStatus int not null,
    dataPedido datetime not null default getdate(),
    
);
GO
create table itensPedido(
    id int not null IDENTITY(1,1) primary key,
    idPedido int not null,
    idProduto int not null,
    quantidade int not null,
    precoUnitario DECIMAL(15,4) not null,
);
GO
create table pagamentos(
    id int not null IDENTITY(1,1) primary key,
    idPedido int not null,
    valor DECIMAL(15,4) not null,
    idformapagamento varchar(50) not null,
    dataPagamento datetime not null default getdate(),

);
GO
create table funcionarios(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    cargo varchar(50) not null,
);
GO
CREATE TABLE statusPedido(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
);
GO
create table formaPagamento(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
);
