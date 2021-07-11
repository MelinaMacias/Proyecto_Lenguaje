
package ec.edu.espol.lpgrupo8.services;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CheckerService {

    private String result;
    
    public String getTokenCheck(String code) {

        this.result = "";
        runCommand("python code/main.py ", code, "\n");
        
        return this.result;
        
    }
    
    public String getSyntaxCheck(String code) {

        this.result = "";
        runCommand("python code/analizador_sintactico.py", code, "\n");

        return this.result;

    }

    private void runCommand(String command, String code, String splitStr) {
        
        String arguments = "";
        for(String line : code.split(splitStr)) {
            arguments += String.format("\"%s\" ", line); }
        Process process = null;
        String execution = String.format("%s %s", command, arguments);

        try  {
            
            process = Runtime.getRuntime().exec(execution);
            new BufferedReader( new InputStreamReader(process.getInputStream()) )
                .lines().forEach( (line) -> { this.result += line; });
            
        } catch (IOException e) {
            System.out.println( e.getMessage() ); }
    
    }
    
}
