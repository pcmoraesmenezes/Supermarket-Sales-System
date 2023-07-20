package pdv;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import pdv.dominio.Registradora;
import pdv.dominio.excecoes.DescricaoProdutoInexistente;

public class PDVInterface extends Application {

    private Registradora registradora;
    private TextField quantidadeField;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Inicialize a registradora e outras instâncias necessárias aqui
        registradora = new Registradora("R01");

        primaryStage.setTitle("PDV Interface");
        VBox root = new VBox(10);
        root.setPadding(new Insets(20, 20, 20, 20));

        Label titleLabel = new Label("Supermercado Preço Bão");
        titleLabel.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");
        Label quantityLabel = new Label("Quantidade:");
        quantidadeField = new TextField();

        ListView<String> productList = new ListView<>();
        // Carregue a lista de produtos disponíveis para venda aqui (a partir do CatalogoProdutos)

        Button addButton = new Button("Adicionar à Venda");
        addButton.setOnAction(e -> adicionarItemVenda(productList.getSelectionModel().getSelectedItem()));

        Button finalizeButton = new Button("Finalizar Venda");
        finalizeButton.setOnAction(e -> finalizarVenda());

        VBox.setMargin(titleLabel, new Insets(0, 0, 10, 0));
        VBox.setMargin(productList, new Insets(0, 0, 10, 0));
        VBox.setMargin(addButton, new Insets(0, 0, 5, 0));

        root.getChildren().addAll(titleLabel, productList, quantityLabel, quantidadeField, addButton, finalizeButton);

        Scene scene = new Scene(root, 400, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void adicionarItemVenda(String descricaoProduto) {
        try {
            int quantidade = Integer.parseInt(quantidadeField.getText());
            registradora.entrarItem(descricaoProduto, quantidade);
            // Atualize a interface para mostrar os itens adicionados à venda
        } catch (NumberFormatException | DescricaoProdutoInexistente ex) {
            ex.printStackTrace();
            // Trate possíveis exceções aqui, se necessário
        }
    }

    private void finalizarVenda() {
        registradora.finalizarVenda();
        // Faça o processamento final da venda e exiba um recibo ou outra saída
    }
}
