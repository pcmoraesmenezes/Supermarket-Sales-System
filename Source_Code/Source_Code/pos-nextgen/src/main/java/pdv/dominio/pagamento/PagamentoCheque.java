package pdv.dominio.pagamento;
 
public class PagamentoCheque extends Pagamento {
   
    private String banco;

    public PagamentoCheque(double quantiaFornecida, String banco)  {
        super(quantiaFornecida);       
        this.banco = banco;
    }
    
    public String getBanco() {
        return banco;
    }

    public void setBanco(String banco) {
        this.banco = banco;
    }    
    
    @Override
    public String toString() {
        return "Tipo de pagamento...: Cheque\n" +
                "Quantia fornecida....: R$ " + super.getQuantiaFornecida() + "\n"
                + "Banco................: " + banco;
    }  
}
