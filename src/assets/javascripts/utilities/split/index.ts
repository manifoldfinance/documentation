/*
 * Copyright (c) 2016-2021 Martin Donath <martin.donath@squidfunk.com>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 */

/* ----------------------------------------------------------------------------
 * Types
 * ------------------------------------------------------------------------- */

/**
 * Range
 */
export type Range = [number, number]

/* ----------------------------------------------------------------------------
 * Helper types
 * ------------------------------------------------------------------------- */

/**
 * Visitor function
 *
 * @param range - Range
 */
type VisitorFn = (range: Range) => void

/* ----------------------------------------------------------------------------
 * Functions
 * ------------------------------------------------------------------------- */

/**
 * Split a string using the given separator
 *
 * @param value - String value
 * @param separator - Separator
 * @param fn - Visitor function
 */
export function split(
  value: string, separator: RegExp | string, fn: VisitorFn
): void {
  separator = new RegExp(separator, "g")

  /* Split string using separator */
  let match: RegExpExecArray | null
  let index = 0
  do {
    match = separator.exec(value)

    /* Emit non-empty range */
    const until = match ? match.index : value.length
    if (index < until)
      fn([index, until])

    /* Update last index */
    if (match) {
      const [term] = match
      index = match.index + term.length

      /* Support zero-length lookaheads */
      if (term.length === 0)
        separator.lastIndex = match.index + 1
    }
  } while (match)
}
