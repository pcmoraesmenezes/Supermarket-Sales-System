package pdv.dominio.servicos;

public interface CalculadoraFinanceira {
    double calcularMontanteComJuros(double montanteInicial, int periodoMeses, double jurosAoMes);
}
