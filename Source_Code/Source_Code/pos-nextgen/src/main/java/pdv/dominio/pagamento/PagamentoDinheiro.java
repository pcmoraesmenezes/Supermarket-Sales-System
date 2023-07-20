package pdv.dominio.pagamento;

public class PagamentoDinheiro extends Pagamento  {
    
    public PagamentoDinheiro(double quantia)  {
       super(quantia);
    }    

    @Override
    public String toString() {
        return "Tipo de pagamento...: Dinheiro\n" + 
               super.toString();
    }
}
