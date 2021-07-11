
package ec.edu.espol.lpgrupo8.models;

import java.util.List;

import lombok.Data;

@Data
public class CodeLine {
    
    private int lineNumber;
    private List<Token> tokens;

    @Override
    public String toString() {

        String parseTokens = "";

        int index = 1;
        for(Token token : this.tokens) { 
    
            parseTokens += String.format(
                "\tToken %d: \n\t\tID: %s \n\t\tColumna: %d \n\t\tValor: %s\n\n",
                index++,
                token.getId(),
                token.getColnumber(),
                token.getValue()
            );
        
        }
        
        return String.format("Linea %d: \n %s", this.lineNumber, parseTokens);
    
    }
    
}
