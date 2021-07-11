
package ec.edu.espol.lpgrupo8.models;

import java.util.List;

import lombok.Data;

@Data
public class ExecutionResult {
    
    private List<CodeLine> lines;
    private List<String> errors;

}
