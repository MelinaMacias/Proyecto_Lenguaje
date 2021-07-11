
package ec.edu.espol.lpgrupo8.controllers;

import java.net.URL;
import java.util.ResourceBundle;

import ec.edu.espol.lpgrupo8.services.DisplayService;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Hyperlink;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;

public class UIController implements Initializable {

    private DisplayService displayService;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        
        viewPicker.setItems(
			FXCollections.observableArrayList("Vista TOKENS", "Vista AST") );

        displayService = new DisplayService(resultView, errorView);
        reloadBtn.setDisable(true);
        
    }

    @FXML
    public void changeView() {
        
        viewLabel.setText( viewPicker.getValue() );
        reloadBtn.setDisable(false);
        
        try {

            if(viewPicker.getValue().equals("Vista TOKENS")) {
                displayService.showTokenCheck( codeInput.getText() ); }
            else {
                displayService.showSyntaxCheck( codeInput.getText() ); }

        } catch ( Exception e ){
            e.printStackTrace(); }

    }
    
    public void reloadChecker() {
    
        changeView();
    
    }
    
    @FXML
    Label viewLabel;

    @FXML
    Hyperlink reloadBtn;
    
    @FXML
    TextArea codeInput;

    @FXML
    TextArea errorView;
    
    @FXML
    TextArea resultView;
    
    @FXML
    ComboBox<String> viewPicker;
    
}
