import interface as fc
import lex as lxc
from lex import tokens
import sintaxis as sntx

fc.create_interface ()
# lex.test_Sergio_Basurto()
# lex.test_Ramon_Macias()

s = '''
5 < 6
            8 > 10
            7 <= 9
            8 >= 9
            let i = 5.
            let f = 56
            let mut n = -7.
            let n = -7.5
            fn main() {
                // Variables
                let mut counter = 0;
                let my_string = String::from("Hola, mundo!");
                let my_float = 3.14;

                // While loop
                while counter < 5 {
                    println!("Contador: {}", counter);
                    counter += 1;
                }

                // For loop
                for i in 0..5 {
                    println!("Valor de i: {}", i);
                }

                // If statement
                if my_string.len() > 10 {
                    println!("La cadena es larga");
                } else {
                    println!("La cadena es corta");
                }

                // Mostrar valores
                println!("Cadena: {}", my_string);
                println!("Flotante: {}", my_float);
            }
'''
n = """
    max ();
    5 > 6;
    println ( "hola mundo" );
    1 >= 3;
    1 == 2;
    2 > 4;
    print (4 );
    printarg (4,5); 
    5.6;
    hola;
    7;
    true;
    false;
    True;
    TRUE;
    False;
    FALSE;
    "hola mundo";
    'h';
    true || false;
    hola();
    5 < 6;
    8 > 10;
    7 <= 9;
    8 >= 9;
    6 == 8;
    6 != 6;
    if my_string.len() > 10 {
                    println("La cadena es larga");
                } else {
                    println("La cadena es corta");
                }
    """
    
lxc.test_lex(n)
sntx.test_sintaxis(n)