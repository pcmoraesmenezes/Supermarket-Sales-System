package pdv;

import pdv.dominio.servicos.CalculadoraFinanceira;
import pdv.dominio.servicos.CalculadoraJurosCompostos;
import pdv.dominio.servicos.CalculadoraJurosSimples;

public class TesteCalculadoraFinanceira {
    public static void main(String [] args) {
        double montanteInicial = 10000;
        int periodoMeses = 3;
        double jurosAoMes = 0.05;
        
        CalculadoraFinanceira calculadora = new CalculadoraJurosCompostos();
        System.out.println("************* Cálculo de juros  com calculadora de juros compostos **********************");
        System.out.println("Montante inicial..: " + montanteInicial);
        System.out.println("Período em meses...: " + periodoMeses);
        System.out.println("Juros ao mes......:  " + jurosAoMes);
        System.out.println("Objeto calculadora..: " + calculadora);
        System.out.println("Total..: " + calculadora.calcularMontanteComJuros(montanteInicial, periodoMeses, jurosAoMes));
        System.out.println("*****************************************************");
        
        calculadora = new CalculadoraJurosSimples();
        System.out.println("************* Cálculo de juros com calculadora de juros simples  **********************");
        System.out.println("Montante inicial..: " + montanteInicial);
        System.out.println("Período em meses...: " + periodoMeses);
        System.out.println("Juros ao mes......:  " + jurosAoMes);
        System.out.println("Objeto calculadora..: " + calculadora);
        System.out.printf("Total..: " + calculadora.calcularMontanteComJuros(montanteInicial, periodoMeses, jurosAoMes));
        System.out.println("*****************************************************");
    }
}
