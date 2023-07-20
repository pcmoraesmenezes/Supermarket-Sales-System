package pdv.dominio.pagamento;

public abstract class Pagamento {  
    private double quantiaFornecida;

    public Pagamento(double quantiaFornecida) {
       this.quantiaFornecida = quantiaFornecida;
    }

    public double getQuantiaFornecida() {
        return quantiaFornecida;
    }
    
    public void setQuantiaFornecida(double quantia) {
        this.quantiaFornecida = quantia;    
    }
    
    @Override
    public String toString() {
        return "Quantia Fornecida: R$ " + quantiaFornecida;
    }   
}
