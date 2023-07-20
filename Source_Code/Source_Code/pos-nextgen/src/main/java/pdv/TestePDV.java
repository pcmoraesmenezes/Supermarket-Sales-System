package pdv;

import pdv.dominio.*;
import pdv.dominio.excecoes.DescricaoProdutoInexistente;
import pdv.dominio.pagamento.Operadora;


public class TestePDV {

    public static void main(String[] args) {

        Endereco endereco = new Endereco("Rua X", "", 5, "Alfenas", "Aeroporto", "MG", "37130-000");
        Loja loja = new Loja("Supermercado Preço Bão", endereco);

        try {
           	// Criando uma venda com cartão, uma parcela na primeira registradora
        	    // entrarItem de Registradora pode lancar uma excecao DescricaoProdutoInexistente
            Registradora registradora = loja.getRegistradora("R01");
            registradora.criarNovaVenda();

            registradora.entrarItem("01", 3);
            registradora.entrarItem("02", 2);
            registradora.entrarItem("03", 1);

            registradora.finalizarVenda();

            // TODO troco como retorno de fazer pagamento?
            double totalVenda = registradora.getVendaCorrente().calcularTotalVenda();
            registradora.fazerPagamento(totalVenda, Operadora.AMERICAN, 1, TipoCalculadora.JUROS_SIMPLES);

            // 0.0 eh o troco a ser devolvido
            gerarRecibo(registradora, 0.0);

            // Criando uma venda com pagamento em dinheiro na segunda registradora
            Registradora registradora2 = loja.getRegistradora("R02");
            registradora2.criarNovaVenda();

            registradora2.entrarItem("08", 3);
            registradora2.entrarItem("01", 2);
            registradora2.entrarItem("09", 1);

            registradora2.finalizarVenda();

            registradora2.fazerPagamento(100.00);

            // troco (200 fornecidos - valor total da venda)
            gerarRecibo(registradora2, 100 - registradora2.getVendaCorrente().calcularTotalVenda());

            // Criando uma venda com cheque na terceira registradora
            Registradora registradora3 = loja.getRegistradora("R02");

            registradora3.criarNovaVenda();
            registradora3.entrarItem("06", 3);
            registradora3.entrarItem("07", 2);
        		registradora3.entrarItem("02", 1);
        		registradora3.finalizarVenda();
        		registradora3.fazerPagamento(registradora3.getVendaCorrente().calcularTotalVenda(), "Banco do Brasil");

            // 0.0 eh o troco a ser devolvido
            gerarRecibo(registradora3, 0.0);

        } catch (DescricaoProdutoInexistente d) {
            System.out.println(d.getMessage());
        }
    }

    public static void gerarRecibo(Registradora registradora, double troco) {
        Venda venda = registradora.getVendaCorrente();
        System.out.println("");
        System.out.println("--------------------------- Supermercado Preço Bão ---------------------------");
        System.out.println("                             Registradora : " + registradora.getId());
        System.out.println("\t\t\t\tCUPOM FISCAL");
        System.out.println(venda);
        System.out.println("Troco................: R$ " + troco);
    }
}
