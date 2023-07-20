package pdv.dominio;

public class Endereco {
    private String logradouro;
    private String complemento;
    private int numero;
    private String cidade;
    private String bairro;
    private String uf;
    private String cep;   

    public Endereco(String logradouro, String complemento, int numero, String cidade, String bairro, String uf, String cep) {
        this.logradouro = logradouro;
        this.complemento = complemento;
        this.numero = numero;
        this.cidade = cidade;
        this.bairro = bairro;
        this.uf = uf;
        this.cep = cep;
    }    
    
    public String getLogradouro() {
        return logradouro;
    }

    public void setLogradouro(String logradouro) {
        this.logradouro = logradouro;
    }

     
    public String getComplemento() {
        return complemento;
    }

    public void setComplemento(String complemento) {
        this.complemento = complemento;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getUf() {
        return uf;
    }

    public void setUf(String uf) {
        this.uf = uf;
    }

    public String getCep() {
        return cep;
    }

    public void setCep(String cep) {
        this.cep = cep;
    }
}
