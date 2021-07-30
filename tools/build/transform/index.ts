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

import { createHash } from "crypto"
import { build as esbuild } from "esbuild"
import * as path from "path"
import postcss from "postcss"
import {
  NEVER,
  Observable,
  concat,
  defer,
  of
} from "rxjs"
import {
  catchError,
  endWith,
  ignoreElements,
  switchMap
} from "rxjs/operators"
import { render as sass } from "sass"
import { promisify } from "util"

import { base, mkdir, write } from "../_"

/* ----------------------------------------------------------------------------
 * Helper types
 * ------------------------------------------------------------------------- */

/**
 * Transform options
 */
interface TransformOptions {
  from: string                         /* Source destination */
  to: string                           /* Target destination */
}

/* ----------------------------------------------------------------------------
 * Helper functions
 * ------------------------------------------------------------------------- */

/**
 * Compute a digest for cachebusting a file
 *
 * @param file - File
 * @param data - File data
 *
 * @returns File with digest
 */
function digest(file: string, data: string): string {
  if (process.argv.includes("--optimize")) {
    const hash = createHash("sha256").update(data).digest("hex")
    return file.replace(/\b(?=\.)/, `.${hash.slice(0, 8)}.min`)
  } else {
    return file
  }
}

/* ----------------------------------------------------------------------------
 * Functions
 * ------------------------------------------------------------------------- */

/**
 * Transform a stylesheet
 *
 * @param options - Options
 *
 * @returns File observable
 */
export function transformStyle(
  options: TransformOptions
): Observable<string> {
  return defer(() => promisify(sass)({
    file: options.from,
    outFile: options.to,
    includePaths: [
      "src/assets/stylesheets",
      "node_modules/modularscale-sass/stylesheets",
      "node_modules/material-design-color",
      "node_modules/material-shadows"
    ]
  }))
    .pipe(
      switchMap(({ css }) => postcss([
        require("autoprefixer"),
        require("postcss-inline-svg")({
          paths: [
            `${base}/.icons`
          ],
          encode: false
        }),
        ...process.argv.includes("--optimize")
          ? [require("cssnano")]
          : []
      ])
        .process(css, {
          from: options.from
        })
      ),
      catchError(err => {
        console.log(err.formatted || err.message)
        return NEVER
      }),
      switchMap(({ css }) => {
        const file = digest(options.to, css)
        return concat(
          mkdir(path.dirname(file)),
          write(`${file}`, css.replace(
            options.from,
            path.basename(file)
          ))
        )
          .pipe(
            ignoreElements(),
            endWith(file)
          )
      })
    )
}

/**
 * Transform a script
 *
 * @param options - Options
 *
 * @returns File observable
 */
export function transformScript(
  options: TransformOptions
): Observable<string> {
  return defer(() => esbuild({
    entryPoints: [options.from],
    target: "es2015",
    write: false,
    bundle: true,
    sourcemap: false,
    legalComments: "none",
    minify: process.argv.includes("--optimize")
  }))
    .pipe(
      switchMap(({ outputFiles: [file] }) => {
        return of({
          js:  file.text,
          map: null
        })
      }),
      switchMap(({ js }) => {
        const file = digest(options.to, js)
        return concat(
          mkdir(path.dirname(file)),
          write(`${file}`, js)
        )
          .pipe(
            ignoreElements(),
            endWith(file)
          )
      })
    )
}
