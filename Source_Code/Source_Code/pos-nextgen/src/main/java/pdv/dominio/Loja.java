package pdv.dominio;

import java.util.ArrayList;
import java.util.List;

public class Loja {
    private String nome;
     private List<Venda> vendas;
     private List<Registradora> registradoras;
     
    private Endereco endereco;
    
    public Loja(String nome, Endereco endereco) {
        this.nome = nome;
        registradoras = new ArrayList<>();
        this.endereco = endereco;  
        
        Registradora r1 = new Registradora("R01");
        Registradora r2 = new Registradora("R02");
        Registradora r3 = new Registradora("R03"); 
        
        adicionarRegistradora(r1);
        adicionarRegistradora(r2);
        adicionarRegistradora(r3);
    }

    public void adicionarVenda(Venda v) {
    	vendas.add(v);
    }

    public void adicionarRegistradora(Registradora registradora) {
    	registradoras.add(registradora);
    }

    public Venda getUltimaVenda() {
        return vendas.get(vendas.size()-1);
    }

    public Registradora getRegistradora(String id) {
        Registradora temp = null;
        for (Registradora r: registradoras){
            if (r.getId().equals(id))
                temp = r;
        }
        return temp;
    }

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public Endereco getEndereco() {
		return endereco;
	}

	public void setEndereco(Endereco endereco) {
		this.endereco = endereco;
	}
}
