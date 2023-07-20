package pdv;


import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

public class IntefaceF extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("PDV Interface");

        // Elementos da interface
        Label itemLabel = new Label("Item:");
        ComboBox<String> itemComboBox = new ComboBox<>();
        itemComboBox.getItems().addAll("Chocolate Talento", "Chiclete Trident", "Lata de Coca-cola", "Outros itens...");

        Label quantidadeLabel = new Label("Quantidade:");
        TextField quantidadeTextField = new TextField();

        Label tipoPagamentoLabel = new Label("Tipo de Pagamento:");
        ComboBox<String> tipoPagamentoComboBox = new ComboBox<>();
        tipoPagamentoComboBox.getItems().addAll("Dinheiro", "Cartão de Crédito", "Cheque");

        Button adicionarButton = new Button("Adicionar à Venda");

        // Lógica para adicionar o item à venda quando o botão é clicado
        adicionarButton.setOnAction(e -> {
            // Aqui você pode adicionar a lógica para adicionar o item à venda conforme o selecionado nos ComboBoxes
            // Por exemplo, chamar os métodos necessários nas classes do seu PDV.
            // Exemplo: String selectedItem = itemComboBox.getValue();
            //          int quantidade = Integer.parseInt(quantidadeTextField.getText());
            //          pdv.adicionarItem(selectedItem, quantidade);
        });

        // Layout da interface
        VBox layout = new VBox(10);
        layout.getChildren().addAll(itemLabel, itemComboBox, quantidadeLabel, quantidadeTextField, tipoPagamentoLabel,
                tipoPagamentoComboBox, adicionarButton);

        Scene scene = new Scene(layout, 300, 200);
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
