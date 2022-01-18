Os alunos da escola primária geralmente organizam problemas aritméticos de modo vertical para facilitar a sua resolução. Por exemplo, "235 + 52" se torna:

![image](https://user-images.githubusercontent.com/18738176/149987672-c9913f9c-5c15-4857-95d1-ae54364950e6.png)

Crie uma função que receba uma lista de strings que sejam problemas aritméticos e retorne os problemas dispostos verticalmente e lado a lado. A função deve, como opção, receber um segundo argumento. Quando o segundo argumento for definido como True, as respostas devem ser exibidas.

Exemplo
Chamada da função:

![image](https://user-images.githubusercontent.com/18738176/149987756-f8fa7f8b-2fcb-44a3-9a8a-4a4c7772a4f3.png)

Resultado:

![image](https://user-images.githubusercontent.com/18738176/149987804-48c528ad-7896-4064-b011-f0839efcb2ba.png)

Chamada da função:

![image](https://user-images.githubusercontent.com/18738176/149988052-bd14156f-4b71-4145-b048-842d2d5c648d.png)

Resultado:

![image](https://user-images.githubusercontent.com/18738176/149988094-62a1cba5-539f-4611-9d24-71035819ca0b.png)

Regras

A função retornará a conversão correta se os problemas fornecidos forem formatados corretamente. Caso contrário, ela retornará uma string que descreve um erro significativo para o usuário.

* Situações que retornarão um erro:
  * Se houver muitos problemas fornecidos para a função. O limite é 5. Qualquer outro número retornará: Error: Too many problems.
  * Os operadores apropriados que a função aceitará são adição e subtração. A multiplicação e a divisão retornarão um erro. Outros operadores não mencionados aqui não precisarão ser testados. O erro retornado será: Error: Operator must be '+' or '-'.
  * Cada número (operando) deve conter apenas algarismos. Caso contrário, a função retornará: Error: Numbers must only contain digits.
  * Cada operando (ou seja, o número de cada lado do operador) tem, no máximo, quatro algarismos. Do contrário, a string de erro retornada será: Error: Numbers cannot be more than four digits.
* Se o usuário forneceu o formato correto dos problemas, a conversão retornada seguirá estas regras:
  * Deve haver um único espaço entre o operador e o maior entre os dois operandos. O operador estará na mesma linha do segundo operando. Ambos os operadores estarão na mesma ordem fornecida - o primeiro será o de cima e o segundo será o de baixo.
  * Os números devem estar alinhados à direita.
  * Deve haver quatro espaços entre cada problema.
  * Deve haver travessões abaixo de cada problema. Os travessões devem compreender todo o tamanho de cada problema individualmente. (O exemplo acima mostra como deve ser a aparência do resultado.)
