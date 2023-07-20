package pdv.dominio;

public class ItemVenda {
    private DescricaoProduto descricaoProduto;
    private int quantidade;

    ItemVenda(DescricaoProduto descricaoProduto, int quantidade) {
        this.quantidade = quantidade;
        this.descricaoProduto = descricaoProduto;
    }

    public int getQuantidade() {
        return quantidade;
    }   

    public DescricaoProduto getDescricaoProduto() {
        return descricaoProduto;
    }  
    
    private double getSubtotal() {
        return quantidade * descricaoProduto.getPreco();
    }

    @Override
    public String toString() {
        return descricaoProduto + "\t    " + quantidade + "  \t\t" + getSubtotal() +'\n';
    }   
}
