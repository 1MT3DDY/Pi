const Parser = window.exprEval.Parser;
const parser = new Parser();
const numbers = document.getElementsByClassName("number");
const operators = document.getElementsByClassName("operator");
const display = document.getElementById("display");
const clearAll = document.getElementById("clear-all");
const clear = document.getElementById("clear");
const equal = document.getElementById("equal");
const operatorsCharacters = ["*", "+", "-", "/"];
const dot = document.getElementById("dot");
const parenthesesOpen = document.getElementById("parentheses-open");
const parenthesesClose = document.getElementById("parentheses-close");
let openParenthesesCount = 0;
let lastOperator = false;
display.value = "0";

const setValue = (val) => {
    display.value = val;
    display.innerText = display.value;
};

for (let i = 0; i < numbers.length; i++) {
    numbers[i].addEventListener("click", (e) => {
        let value = e.target.innerText;
        if (display.value !== "0") {
            value = display.value + value;
        }

        setValue(value);
        lastOperator = false;
    });
}

clearAll.addEventListener("click", () => {
    setValue("0");
    lastOperator = false;
});

clear.addEventListener("click", () => {
    if (display.value.length === 1) return setValue("0");
    var lastChar = display.value.slice(-1);
    if (operatorsCharacters.includes(lastChar)) {
        lastOperator = false;
    }

    if (lastChar === ")") {
        openParenthesesCount++;
    }
    if (lastChar === "(") {
        openParenthesesCount--;
    }

    setValue(display.value.slice(0, -1));
});

for (let i = 0; i < operators.length; i++) {
    operators[i].addEventListener("click", (e) => {
        let value = "";
        if (lastOperator || display.innerText === "0") return;
        switch (e.target.innerText) {
            case "asterisk":
                value = "*";
                break;
            case "add":
                value = "+";
                break;
            case "remove":
                value = "-";
                break;
            case "pen_size_1":
                value = "/";
                break;
        }

        setValue(display.value + value);
        lastOperator = true;
    });
}

const getCurrentNumber = () => {
    const parts = display.value.split(/[\+\-\*\/]/);
    return parts[parts.length - 1];
};

dot.addEventListener("click", () => {
    const currentNumber = getCurrentNumber();
    if (currentNumber.includes(".")) return;
    setValue(display.value + ".");
});

parenthesesOpen.addEventListener("click", () => {
    var numbers = "0123456789";
    var lastChar = display.value.slice(-1);

    if ((display.value !== "0" && numbers.includes(lastChar)) || lastChar === ")")
        return;

    let value = "(";
    if (display.value !== "0") {
        value = display.value + value;
    }

    setValue(value);
    openParenthesesCount++;
});

parenthesesClose.addEventListener("click", () => {
    if (openParenthesesCount <= 0) return;
    setValue(display.value + ")");
    openParenthesesCount--;
});

equal.addEventListener("click", () => {
    try {
        let result = parser.evaluate(display.value);
        setValue(result);
    } catch (e) {
        console.error("ExpresiÃ³n invalida: ", e.message);
        setValue("Sintax Error");
    }
});