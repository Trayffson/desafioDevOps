CREATE TABLE IF NOT EXISTS deploy.deploy_api (
    deploy_id INT AUTO_INCREMENT PRIMARY KEY,
    componente VARCHAR(100) NOT NULL,
    versao float,
    responsavel VARCHAR(50),
    status VARCHAR(50),
    data TIMESTAMP
)  ENGINE=INNODB;
