/** @emdad-module **/

import * as spreadsheet from "@emdad/o-spreadsheet";

const { parseTokens, iterateAstNodes } = spreadsheet;

/**
 * @typedef {Object} emdadFunctionDescription
 * @property {string} functionName Name of the function
 * @property {Array<string>} args Arguments of the function
 *
 * @typedef {Object} Token
 * @property {string} type
 * @property {string} value

 */

/**
 * This function is used to search for the functions which match the given matcher
 * from the given formula
 *
 * @param {Token[]} tokens
 * @param {string[]} functionNames e.g. ["emdad.LIST", "emdad.LIST.HEADER"]
 * @private
 * @returns {Array<emdadFunctionDescription>}
 */
export function getemdadFunctions(tokens, functionNames) {
    // Parsing is an expensive operation, so we first check if the
    // formula contains one of the function names
    if (!tokens.some((t) => t.type === "SYMBOL" && functionNames.includes(t.value.toUpperCase()))) {
        return [];
    }
    let ast;
    try {
        ast = parseTokens(tokens);
    } catch {
        return [];
    }
    return _getemdadFunctionsFromAST(ast, functionNames);
}

/**
 * This function is used to search for the functions which match the given matcher
 * from the given AST
 *
 * @param {Object} ast (see o-spreadsheet)
 * @param {string[]} functionNames e.g. ["emdad.LIST", "emdad.LIST.HEADER"]
 *
 * @private
 * @returns {Array<emdadFunctionDescription>}
 */
function _getemdadFunctionsFromAST(ast, functionNames) {
    return iterateAstNodes(ast)
        .filter((ast) => ast.type === "FUNCALL" && functionNames.includes(ast.value.toUpperCase()))
        .map((ast) => ({ functionName: ast.value.toUpperCase(), args: ast.args }));
}
