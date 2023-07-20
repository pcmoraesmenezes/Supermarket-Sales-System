package pdv.dominio.excecoes;

public class DescricaoProdutoInexistente extends Exception {
    private static final long serialVersionUID = 1L;
	private String id;
    
    public DescricaoProdutoInexistente(String mensagem, String id) {
        super(mensagem);
        this.id = id;       
    }

    public DescricaoProdutoInexistente(String string, Throwable throwable) {
        super(string, throwable);
    }

    public DescricaoProdutoInexistente(String string) {
        super(string);
    }

    public DescricaoProdutoInexistente() {
        super();
    }

    public String toString() {
        return super.toString() + "\n" +
               "ID....: " + this.id;
    }
}
