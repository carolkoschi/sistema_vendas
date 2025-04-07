use sistema_vendas;
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='clientes' AND xtype='U')
create table clientes
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    email varchar(150) unique not null,
    telefone varchar(20) not null,
    dataCadastro datetime not null default getdate()
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='endereco' AND xtype='U')
create table endereco
(
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
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='tipoEndereco' AND xtype='U')
CREATE TABLE tipoEndereco
(
    id int not null IDENTITY(1,1) primary key,
    nome VARCHAR(50) not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='clienteEndereco' AND xtype='U')
create table clienteEndereco
(
    id int not null IDENTITY(1,1) primary key,
    idCliente int not null,
    idEndereco int not null,
    idTipoEndereco int not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='produtos' AND xtype='U')
create table produtos
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    preco decimal(15,4) not null,
    estoque int not null,
    idcategoria int not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='categoria' AND xtype='U')
create table categoria
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='pedidos' AND xtype='U')
create table pedidos
(
    id int not null IDENTITY(1,1) primary key,
    idCliente int not null,
    IdFuncionario int not null,
    idStatus int not null,
    dataPedido datetime not null default getdate(),

);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='itensPedido' AND xtype='U')
create table itensPedido
(
    id int not null IDENTITY(1,1) primary key,
    idPedido int not null,
    idProduto int not null,
    quantidade int not null,
    precoUnitario DECIMAL(15,4) not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='pagamentos' AND xtype='U')
create table pagamentos
(
    id int not null IDENTITY(1,1) primary key,
    idPedido int not null,
    valor DECIMAL(15,4) not null,
    idformapagamento varchar(50) not null,
    dataPagamento datetime not null default getdate(),

);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='funcionarios' AND xtype='U')
create table funcionarios
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    cargo varchar(50) not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='statusPedido' AND xtype='U')
CREATE TABLE statusPedido
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='formaPagamento' AND xtype='U')
create table formaPagamento
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
);
GO
IF NOT EXISTS (SELECT *
FROM sysobjects
WHERE name='usuarios' AND xtype='U')
CREATE TABLE usuarios
(
    id int not null IDENTITY(1,1) primary key,
    nome varchar(100) not null,
    email varchar(150) unique not null,
    senha varchar(255) not null,
    dataCadastro datetime not null default getdate(),
);
