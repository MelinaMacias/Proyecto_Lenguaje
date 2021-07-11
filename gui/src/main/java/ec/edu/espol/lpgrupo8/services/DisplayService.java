
package ec.edu.espol.lpgrupo8.services;

import java.util.List;

import com.fasterxml.jackson.databind.ObjectMapper;

import ec.edu.espol.lpgrupo8.models.CodeLine;
import ec.edu.espol.lpgrupo8.models.ExecutionResult;
import javafx.scene.control.TextArea;

/**
 * Display Service
 */
public class DisplayService { 

    private CheckerService checkerService;

    ObjectMapper mapper;

    private TextArea resultView;
    private TextArea errorView;
    private ExecutionResult checkResult;

    public DisplayService(
        ExecutionResult result, TextArea resultView, 
        TextArea errorView) {
        
        this.resultView = resultView;
        this.errorView = errorView;
        this.checkResult = result;

        this.mapper = new ObjectMapper(); 
        this.checkerService = new CheckerService();

    }
    
    

    public DisplayService(TextArea resultView, TextArea errorView) {
    
        this.resultView = resultView;
        this.errorView = errorView;
        
        this.mapper = new ObjectMapper(); 
        this.checkerService = new CheckerService();
    
    }



    public void setCheckResult(ExecutionResult result) {

        this.checkResult = result;

    }

    public void showTokenCheck(String code) throws Exception {
        
        this.checkResult = mapper.readValue(
            checkerService.getTokenCheck(code),
            ExecutionResult.class
        );
        
        errorView.setText("");
        resultView.setText("");
        List<CodeLine> lines = checkResult.getLines();
        for(int idx = 0; idx < lines.size(); idx++) {
        
            lines.get(idx).setLineNumber(idx + 1);
            resultView.appendText( String.format("%s\n", lines.get(idx).toString()) );
        
        }
        
        showErrors();

    }

    public void showSyntaxCheck(String code) throws Exception {

        errorView.setText("");
        this.checkResult = mapper.readValue(
            checkerService.getSyntaxCheck(code),
            ExecutionResult.class
        );
        
        if( checkResult.getErrors().isEmpty() ) {
            resultView.setText("El código es correcto a nivel sintáctico y semántico"); }
        else {
            resultView.setText("El código no es correcto a nivel sintáctico y semántico"); }

        showErrors();

    }

    private void showErrors() {

        if(checkResult.getErrors() != null){
            
            errorView.setText("");
        
            List<String> errors = checkResult.getErrors();
            for(int idx = 0; idx < errors.size(); idx++) {
                errorView.appendText( 
                    String.format("%s\n", errors.get(idx).toString())); }

        }

    }
    
}
