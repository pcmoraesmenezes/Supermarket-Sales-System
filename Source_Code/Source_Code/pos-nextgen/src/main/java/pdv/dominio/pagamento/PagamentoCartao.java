package pdv.dominio.pagamento;

import pdv.dominio.TipoCalculadora;
import pdv.dominio.servicos.*;

public class PagamentoCartao extends Pagamento implements IJuros {    
    private Operadora operadora;
    private int quantidadeParcelas;   
    private CalculadoraFinanceira calculadora;

    public PagamentoCartao(double quantia, Operadora operadora, int quantidadeParcelas, TipoCalculadora tipoCalculadora) {
        super(quantia);        
        this.operadora = operadora;
        this.quantidadeParcelas = quantidadeParcelas; 
        
        if(tipoCalculadora == TipoCalculadora.JUROS_SIMPLES) {
        		calculadora = new CalculadoraJurosSimples();
        } else if (tipoCalculadora == TipoCalculadora.JUROS_COMPOSTOS) {
        		calculadora = new CalculadoraJurosCompostos();
        }
    }   
    
    public double simularParcelas(double quantia, int quantidadeParcelas) {
        float juros = consultarTaxaJuros();
        double montanteComJuros = calculadora.calcularMontanteComJuros(quantia, quantidadeParcelas, juros);
        return montanteComJuros / quantidadeParcelas;
    }      

    // TODO - Encapsulate what varies
    @Override
    public float consultarTaxaJuros() {
        float taxaJuros = 0.0f;
        switch (quantidadeParcelas) {
            case 1:
                break;
            case 2:
                taxaJuros = 2.5f;
                break;
            case 3:
                taxaJuros = 5.0f;
                break;
            default:
                taxaJuros = 0.0f;
        }
        return taxaJuros;
    }   
    
    @Override
    public String toString() {
        return "Tipo de pagamento...: Cartão de Crédito\n" +
                super.toString() + "\n"
                + "Operadora................: " + operadora + "\n"    
                + "Quantidade de parcelas....: " + quantidadeParcelas + "\n"
                + "Valor de cada parcela...: " + simularParcelas(super.getQuantiaFornecida(), quantidadeParcelas) + "\n"
                + "Tipo de calculadora usada na transação................: " + calculadora.toString()  + "\n" ;
    }
}
