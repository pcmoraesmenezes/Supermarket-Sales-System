package pdv.dominio.servicos;

public class CalculadoraJurosSimples implements CalculadoraFinanceira {

    @Override
    public double calcularMontanteComJuros(double montanteInicial, int periodoMeses, double jurosAoMes) {
        double totalJuros = montanteInicial * periodoMeses * (jurosAoMes * 0.01);
        double novoMontante = montanteInicial + totalJuros;
        return novoMontante;
    }

    @Override
    public String toString() {
        return "Calculadora de juros simples";
    }
    
    
}
