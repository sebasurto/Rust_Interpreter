reserved = {
    'main': 'MAIN',
    'while': 'WHILE',
    'where': 'WHERE',
    'use': 'USE',
    'unsafe': 'UNSAFE',
    'union': 'UNION',
    'type': 'TYPE',
    'trair': 'TRAIT',
    'super': 'SUPER',
    'struct': 'STRUCT',
    'static': 'STATIC',
    'self': 'SELF',
    'Self': 'sELF', #en rust existen dos Self
    'return': 'RETURN',
    'ref': 'REF',
    'pub': 'PUB',
    'mut': 'MUT',
    'move': 'MOVE',
    'mod': 'MOD',
    'match': 'MATCH',
    'loop': 'LOOP',
    'let': 'LET',
    'in': 'IN',
    'impl': 'IMPL',
    'if': 'IF',
    'for': 'FOR',
    'fn': 'FN',
    'extern': 'EXTERN',
    'enum': 'ENUM',
    'else': 'ELSE',
    'dyn': 'DYN',
    'crate': 'CRATE',
    'continue': 'CONTINUE',
    'const': 'CONST',
    'break': 'BREAK',
    'await': 'AWAIT',
    'async': 'ASYNC',
    'as': 'AS',
    'case': 'CASE'
}
code_test = """
    a = 5+6;
    b= -7-5;
    c = 7/8;
    d = 6%7;
    e= 5*6;
    let mut n = 5;
    let jn = 7;
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
    if my_string . len ( ) > 10 {
                    println ( "La cadena es larga" ) ;
                } else {
                    println ( "La cadena es corta" ) ;
                }
    """
code_test_2 = '''
5 < 6;
8 > 10;
7 <= 9;
8 >= 9;
let i = 5.;
let f = 56;
let mut n = -7.;
let n = -7.5;
fn main() {
    // Variables
    let mut counter = 0;
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