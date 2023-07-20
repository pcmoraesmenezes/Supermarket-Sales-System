package pdv.dominio;
 
public class DescricaoProduto {
    private String id;
    private double preco;
    private String descricao;

    DescricaoProduto(String id, double preco, String descricao) {
        this.id = id;
        this.preco = preco;
        this.descricao = descricao;
    }
    
    DescricaoProduto(String id, String descricao) {
        this(id, 0.0, descricao);
    }

    public String getId() {
        return id;
    }   

    public double getPreco() {
        return preco;
    }     
   
    @Override
    public String toString() {
        return descricao + "\t\t" + preco + "\t";
    }

    public boolean equals(Object obj) {
        DescricaoProduto desc = null;
        if ((obj instanceof DescricaoProduto) && (obj != null)) {
           desc = (DescricaoProduto) obj;                                 
           return this.id.equals(desc.getId());
        }
        return false;
    }
}
