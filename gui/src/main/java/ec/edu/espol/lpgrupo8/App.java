
package ec.edu.espol.lpgrupo8;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

/**
 * Main Stage
 *
 */
public class App extends Application {

    @Override
    public void start(Stage mainStage) throws Exception {
        
        Parent root  = FXMLLoader.load( getClass().getResource("/fxml/UI.fxml") );

        Scene mainScene = new Scene(root);

        mainStage.setScene(mainScene);
        mainStage.setResizable(false);
        mainStage.setFullScreen(false);
        mainStage.show();

    }

    public static void main(String[] args) throws Exception {

        launch(args);

    }

}
