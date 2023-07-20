package pdv.dominio.servicos;

public class CalculadoraJurosCompostos implements CalculadoraFinanceira {     

    @Override
    public double calcularMontanteComJuros(double montanteInicial, int periodoMeses, double jurosAoMes) {
        double novoMontante = montanteInicial * Math.pow((1+ jurosAoMes), periodoMeses);
        return novoMontante;
    }
    
    @Override
    public String toString() {
        return "Calculadora de juros compostos";
    }
}
