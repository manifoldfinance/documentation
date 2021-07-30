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

import { Observable } from "rxjs"
import {
  combineLatestWith,
  mapTo,
  shareReplay,
  switchMap,
  tap
} from "rxjs/operators"

import {
  createElement,
  getElementOrThrow,
  request,
  watchScript
} from "~/browser"

import { Component } from "../../../_"

/* ----------------------------------------------------------------------------
 * Types
 * ------------------------------------------------------------------------- */

/**
 * Mermaid code block
 */
export interface MermaidCodeBlock {}

/* ----------------------------------------------------------------------------
 * Data
 * ------------------------------------------------------------------------- */

/**
 * Mermaid instance observable
 */
let mermaid$: Observable<void>

/**
 * Global index for Mermaid integration
 */
let index = 0

/* ----------------------------------------------------------------------------
 * Helper functions
 * ------------------------------------------------------------------------- */

/**
 * Fetch Mermaid styles
 *
 * @returns Mermaid styles observable
 */
function fetchStyles(): Observable<string> {
  const style = getElementOrThrow<HTMLLinkElement>(
    "[rel=preload][href*=mermaid]"
  )
  return request(style.href)
    .pipe(
      switchMap(res => res.text())
    )
}

/* ----------------------------------------------------------------------------
 * Functions
 * ------------------------------------------------------------------------- */

/**
 * Mount Mermaid code block
 *
 * @param el - Code block element
 *
 * @returns Mermaid code block component observable
 */
export function mountMermaidCodeBlock(
  el: HTMLElement
): Observable<Component<MermaidCodeBlock>> {
  mermaid$ ||= watchScript(
    "https://unpkg.com/mermaid@8.8.4/dist/mermaid.min.js"
  )
    .pipe(
      combineLatestWith(fetchStyles()),
      tap(([, themeCSS]) => mermaid.initialize({
        startOnLoad: false,
        themeCSS
      })),
      mapTo(undefined),
      shareReplay(1)
    )

  /* Render diagram */
  mermaid$.subscribe(() => {
    const id = `__mermaid_${index++}`
    const host = createElement("div")
    mermaid.mermaidAPI.render(id, el.innerText, (svg: string) => {

      /* Create a shadow root and inject diagram */
      const shadow = host.attachShadow({ mode: "closed" })
      shadow.innerHTML = svg

      /* Replace code block with diagram */
      el.replaceWith(host)
    })
  })

  /* Create and return component */
  return mermaid$
    .pipe(
      mapTo({ ref: el })
    )
}
