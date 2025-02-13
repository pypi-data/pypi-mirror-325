import { i as ce, a as M, r as ae, b as ue, g as de, w as T, c as fe } from "./Index-BbInrLsP.js";
const y = window.ms_globals.React, ie = window.ms_globals.React.forwardRef, A = window.ms_globals.React.useRef, $ = window.ms_globals.React.useState, F = window.ms_globals.React.useEffect, le = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, me = window.ms_globals.internalContext.useContextPropsContext, pe = window.ms_globals.antd.InputNumber;
var _e = /\s/;
function he(e) {
  for (var t = e.length; t-- && _e.test(e.charAt(t)); )
    ;
  return t;
}
var ge = /^\s+/;
function we(e) {
  return e && e.slice(0, he(e) + 1).replace(ge, "");
}
var U = NaN, be = /^[-+]0x[0-9a-f]+$/i, xe = /^0b[01]+$/i, ye = /^0o[0-7]+$/i, Ee = parseInt;
function q(e) {
  if (typeof e == "number")
    return e;
  if (ce(e))
    return U;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var r = xe.test(e);
  return r || ye.test(e) ? Ee(e.slice(2), r ? 2 : 8) : be.test(e) ? U : +e;
}
var P = function() {
  return ae.Date.now();
}, Ie = "Expected a function", ve = Math.max, Ce = Math.min;
function Re(e, t, r) {
  var i, s, n, o, l, u, p = 0, _ = !1, c = !1, h = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = q(t) || 0, M(r) && (_ = !!r.leading, c = "maxWait" in r, n = c ? ve(q(r.maxWait) || 0, t) : n, h = "trailing" in r ? !!r.trailing : h);
  function m(d) {
    var x = i, O = s;
    return i = s = void 0, p = d, o = e.apply(O, x), o;
  }
  function E(d) {
    return p = d, l = setTimeout(w, t), _ ? m(d) : o;
  }
  function f(d) {
    var x = d - u, O = d - p, V = t - x;
    return c ? Ce(V, n - O) : V;
  }
  function g(d) {
    var x = d - u, O = d - p;
    return u === void 0 || x >= t || x < 0 || c && O >= n;
  }
  function w() {
    var d = P();
    if (g(d))
      return I(d);
    l = setTimeout(w, f(d));
  }
  function I(d) {
    return l = void 0, h && i ? m(d) : (i = s = void 0, o);
  }
  function v() {
    l !== void 0 && clearTimeout(l), p = 0, i = u = s = l = void 0;
  }
  function a() {
    return l === void 0 ? o : I(P());
  }
  function C() {
    var d = P(), x = g(d);
    if (i = arguments, s = this, u = d, x) {
      if (l === void 0)
        return E(u);
      if (c)
        return clearTimeout(l), l = setTimeout(w, t), m(u);
    }
    return l === void 0 && (l = setTimeout(w, t)), o;
  }
  return C.cancel = v, C.flush = a, C;
}
function Se(e, t) {
  return ue(e, t);
}
var ee = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = y, Te = Symbol.for("react.element"), ke = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Pe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, r) {
  var i, s = {}, n = null, o = null;
  r !== void 0 && (n = "" + r), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (o = t.ref);
  for (i in t) je.call(t, i) && !Pe.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Te,
    type: e,
    key: n,
    ref: o,
    props: s,
    _owner: Le.current
  };
}
L.Fragment = ke;
L.jsx = te;
L.jsxs = te;
ee.exports = L;
var b = ee.exports;
const {
  SvelteComponent: Ne,
  assign: z,
  binding_callbacks: G,
  check_outros: Ae,
  children: ne,
  claim_element: re,
  claim_space: Fe,
  component_subscribe: H,
  compute_slots: We,
  create_slot: Me,
  detach: S,
  element: oe,
  empty: K,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Be,
  get_slot_changes: De,
  group_outros: Ve,
  init: Ue,
  insert_hydration: k,
  safe_not_equal: qe,
  set_custom_element_data: se,
  space: ze,
  transition_in: j,
  transition_out: B,
  update_slot_base: Ge
} = window.__gradio__svelte__internal, {
  beforeUpdate: He,
  getContext: Ke,
  onDestroy: Je,
  setContext: Xe
} = window.__gradio__svelte__internal;
function X(e) {
  let t, r;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Me(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var o = ne(t);
      s && s.l(o), o.forEach(S), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(n, o) {
      k(n, t, o), s && s.m(t, null), e[9](t), r = !0;
    },
    p(n, o) {
      s && s.p && (!r || o & /*$$scope*/
      64) && Ge(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        r ? De(
          i,
          /*$$scope*/
          n[6],
          o,
          null
        ) : Be(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      r || (j(s, n), r = !0);
    },
    o(n) {
      B(s, n), r = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function Ye(e) {
  let t, r, i, s, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), r = ze(), n && n.c(), i = K(), this.h();
    },
    l(o) {
      t = re(o, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(S), r = Fe(o), n && n.l(o), i = K(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(o, l) {
      k(o, t, l), e[8](t), k(o, r, l), n && n.m(o, l), k(o, i, l), s = !0;
    },
    p(o, [l]) {
      /*$$slots*/
      o[4].default ? n ? (n.p(o, l), l & /*$$slots*/
      16 && j(n, 1)) : (n = X(o), n.c(), j(n, 1), n.m(i.parentNode, i)) : n && (Ve(), B(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(o) {
      s || (j(n), s = !0);
    },
    o(o) {
      B(n), s = !1;
    },
    d(o) {
      o && (S(t), S(r), S(i)), e[8](null), n && n.d(o);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function Qe(e, t, r) {
  let i, s, {
    $$slots: n = {},
    $$scope: o
  } = t;
  const l = We(n);
  let {
    svelteInit: u
  } = t;
  const p = T(Y(t)), _ = T();
  H(e, _, (a) => r(0, i = a));
  const c = T();
  H(e, c, (a) => r(1, s = a));
  const h = [], m = Ke("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: g
  } = de() || {}, w = u({
    parent: m,
    props: p,
    target: _,
    slot: c,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: g,
    onDestroy(a) {
      h.push(a);
    }
  });
  Xe("$$ms-gr-react-wrapper", w), He(() => {
    p.set(Y(t));
  }), Je(() => {
    h.forEach((a) => a());
  });
  function I(a) {
    G[a ? "unshift" : "push"](() => {
      i = a, _.set(i);
    });
  }
  function v(a) {
    G[a ? "unshift" : "push"](() => {
      s = a, c.set(s);
    });
  }
  return e.$$set = (a) => {
    r(17, t = z(z({}, t), J(a))), "svelteInit" in a && r(5, u = a.svelteInit), "$$scope" in a && r(6, o = a.$$scope);
  }, t = J(t), [i, s, _, c, l, u, o, n, I, v];
}
class Ze extends Ne {
  constructor(t) {
    super(), Ue(this, t, Qe, Ye, qe, {
      svelteInit: 5
    });
  }
}
const Q = window.ms_globals.rerender, N = window.ms_globals.tree;
function $e(e, t = {}) {
  function r(i) {
    const s = T(), n = new Ze({
      ...i,
      props: {
        svelteInit(o) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: o.props,
            slot: o.slot,
            target: o.target,
            slotIndex: o.slotIndex,
            subSlotIndex: o.subSlotIndex,
            ignore: t.ignore,
            slotKey: o.slotKey,
            nodes: []
          }, u = o.parent ?? N;
          return u.nodes = [...u.nodes, l], Q({
            createPortal: W,
            node: N
          }), o.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== s), Q({
              createPortal: W,
              node: N
            });
          }), l;
        },
        ...i.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(r);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const i = e[r];
    return t[r] = nt(r, i), t;
  }, {}) : {};
}
function nt(e, t) {
  return typeof t == "number" && !et.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: o,
          clonedElement: l
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...o]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: o,
      type: l,
      useCapture: u
    }) => {
      r.addEventListener(l, o, u);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: o,
        portals: l
      } = D(n);
      t.push(...l), r.appendChild(o);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function rt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const R = ie(({
  slot: e,
  clone: t,
  className: r,
  style: i,
  observeAttributes: s
}, n) => {
  const o = A(), [l, u] = $([]), {
    forceClone: p
  } = me(), _ = p ? !0 : t;
  return F(() => {
    var E;
    if (!o.current || !e)
      return;
    let c = e;
    function h() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), r && f.classList.add(...r.split(" ")), i) {
        const g = tt(i);
        Object.keys(g).forEach((w) => {
          f.style[w] = g[w];
        });
      }
    }
    let m = null;
    if (_ && window.MutationObserver) {
      let f = function() {
        var v, a, C;
        (v = o.current) != null && v.contains(c) && ((a = o.current) == null || a.removeChild(c));
        const {
          portals: w,
          clonedElement: I
        } = D(e);
        c = I, u(w), c.style.display = "contents", h(), (C = o.current) == null || C.appendChild(c);
      };
      f();
      const g = Re(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(g), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", h(), (E = o.current) == null || E.appendChild(c);
    return () => {
      var f, g;
      c.style.display = "", (f = o.current) != null && f.contains(c) && ((g = o.current) == null || g.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, _, r, i, n, s]), y.createElement("react-child", {
    ref: o,
    style: {
      display: "contents"
    }
  }, ...l);
});
function ot(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function st(e, t = !1) {
  try {
    if (fe(e))
      return e;
    if (t && !ot(e))
      return;
    if (typeof e == "string") {
      let r = e.trim();
      return r.startsWith(";") && (r = r.slice(1)), r.endsWith(";") && (r = r.slice(0, -1)), new Function(`return (...args) => (${r})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function Z(e, t) {
  return le(() => st(e, t), [e, t]);
}
function it({
  value: e,
  onValueChange: t
}) {
  const [r, i] = $(e), s = A(t);
  s.current = t;
  const n = A(r);
  return n.current = r, F(() => {
    s.current(r);
  }, [r]), F(() => {
    Se(e, n.current) || i(e);
  }, [e]), [r, i];
}
const ct = $e(({
  slots: e,
  children: t,
  onValueChange: r,
  onChange: i,
  formatter: s,
  parser: n,
  elRef: o,
  ...l
}) => {
  const u = Z(s), p = Z(n), [_, c] = it({
    onValueChange: r,
    value: l.value
  });
  return /* @__PURE__ */ b.jsxs(b.Fragment, {
    children: [/* @__PURE__ */ b.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ b.jsx(pe, {
      ...l,
      ref: o,
      value: _,
      onChange: (h) => {
        i == null || i(h), c(h);
      },
      parser: p,
      formatter: u,
      controls: e["controls.upIcon"] || e["controls.downIcon"] ? {
        upIcon: e["controls.upIcon"] ? /* @__PURE__ */ b.jsx(R, {
          slot: e["controls.upIcon"]
        }) : typeof l.controls == "object" ? l.controls.upIcon : void 0,
        downIcon: e["controls.downIcon"] ? /* @__PURE__ */ b.jsx(R, {
          slot: e["controls.downIcon"]
        }) : typeof l.controls == "object" ? l.controls.downIcon : void 0
      } : l.controls,
      addonAfter: e.addonAfter ? /* @__PURE__ */ b.jsx(R, {
        slot: e.addonAfter
      }) : l.addonAfter,
      addonBefore: e.addonBefore ? /* @__PURE__ */ b.jsx(R, {
        slot: e.addonBefore
      }) : l.addonBefore,
      prefix: e.prefix ? /* @__PURE__ */ b.jsx(R, {
        slot: e.prefix
      }) : l.prefix,
      suffix: e.suffix ? /* @__PURE__ */ b.jsx(R, {
        slot: e.suffix
      }) : l.suffix
    })]
  });
});
export {
  ct as InputNumber,
  ct as default
};
