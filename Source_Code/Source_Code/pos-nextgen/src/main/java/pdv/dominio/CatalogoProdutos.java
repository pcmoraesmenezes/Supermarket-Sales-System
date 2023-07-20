package pdv.dominio;

import java.util.ArrayList;
import java.util.List;

import pdv.dominio.excecoes.DescricaoProdutoInexistente;

public class CatalogoProdutos {
 	private List<DescricaoProduto> descricoesProdutos;
	private int contadorDescricoesProdutos;
    
    CatalogoProdutos() {
     	descricoesProdutos = new ArrayList<>();
        DescricaoProduto d1 = new DescricaoProduto("01", 3.75, "Chocolate Talento");
        DescricaoProduto d2 = new DescricaoProduto("02", 1.50, "Chiclete Trident");
        DescricaoProduto d3 = new DescricaoProduto("03", 2.50, "Lata de Coca-cola");
        DescricaoProduto d4 = new DescricaoProduto("04", 2.00, "Agua Mineral Caxambu");
        DescricaoProduto d5 = new DescricaoProduto("05", 5.99, "Cerveja Corona extra");
        
        DescricaoProduto d6 = new DescricaoProduto("06", 2.50, "Biscoito cream cracker");
        DescricaoProduto d7 = new DescricaoProduto("07", 4.50, "Leite condensado");
        DescricaoProduto d8 = new DescricaoProduto("08", 18.00, "Cafe Prima Qualitat");
        DescricaoProduto d9 = new DescricaoProduto("09", 2.00, "Danete");
        DescricaoProduto d10 = new DescricaoProduto("10", 1.00, "Bombril");
        
        descricoesProdutos.add(d1);
        descricoesProdutos.add(d2);
        descricoesProdutos.add(d3);
        descricoesProdutos.add(d4);
        descricoesProdutos.add(d5);
        descricoesProdutos.add(d6);
        descricoesProdutos.add(d7);
        descricoesProdutos.add(d8);
        descricoesProdutos.add(d9);
        descricoesProdutos.add(d10);
    }

    public DescricaoProduto getDescricaoProduto(String id) throws DescricaoProdutoInexistente {         
        for (DescricaoProduto desc : descricoesProdutos) {
            if (id.equals(desc.getId()))
                return desc;
        }
        throw new DescricaoProdutoInexistente("Descricao Inexistente para o produto ", id);       
    }
}
