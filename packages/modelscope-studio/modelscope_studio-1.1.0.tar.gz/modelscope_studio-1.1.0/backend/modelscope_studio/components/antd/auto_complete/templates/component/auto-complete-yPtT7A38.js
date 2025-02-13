import { i as de, a as V, r as fe, b as me, g as he, w as O, c as _e } from "./Index-DQBCxCj8.js";
const v = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, W = window.ms_globals.React.useRef, re = window.ms_globals.React.useState, M = window.ms_globals.React.useEffect, H = window.ms_globals.React.useMemo, D = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, T = window.ms_globals.internalContext.ContextPropsProvider, ge = window.ms_globals.internalContext.AutoCompleteContext, Ce = window.ms_globals.antd.AutoComplete, we = window.ms_globals.createItemsContext.createItemsContext;
var xe = /\s/;
function be(e) {
  for (var t = e.length; t-- && xe.test(e.charAt(t)); )
    ;
  return t;
}
var ye = /^\s+/;
function Ee(e) {
  return e && e.slice(0, be(e) + 1).replace(ye, "");
}
var z = NaN, ve = /^[-+]0x[0-9a-f]+$/i, Ie = /^0b[01]+$/i, Re = /^0o[0-7]+$/i, Se = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return z;
  if (V(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = V(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ee(e);
  var r = Ie.test(e);
  return r || Re.test(e) ? Se(e.slice(2), r ? 2 : 8) : ve.test(e) ? z : +e;
}
var A = function() {
  return fe.Date.now();
}, ke = "Expected a function", Oe = Math.max, Pe = Math.min;
function je(e, t, r) {
  var s, o, n, l, i, a, C = 0, h = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(ke);
  t = G(t) || 0, V(r) && (h = !!r.leading, c = "maxWait" in r, n = c ? Oe(G(r.maxWait) || 0, t) : n, g = "trailing" in r ? !!r.trailing : g);
  function u(p) {
    var E = s, k = o;
    return s = o = void 0, C = p, l = e.apply(k, E), l;
  }
  function x(p) {
    return C = p, i = setTimeout(_, t), h ? u(p) : l;
  }
  function d(p) {
    var E = p - a, k = p - C, q = t - E;
    return c ? Pe(q, n - k) : q;
  }
  function m(p) {
    var E = p - a, k = p - C;
    return a === void 0 || E >= t || E < 0 || c && k >= n;
  }
  function _() {
    var p = A();
    if (m(p))
      return b(p);
    i = setTimeout(_, d(p));
  }
  function b(p) {
    return i = void 0, g && s ? u(p) : (s = o = void 0, l);
  }
  function y() {
    i !== void 0 && clearTimeout(i), C = 0, s = a = o = i = void 0;
  }
  function f() {
    return i === void 0 ? l : b(A());
  }
  function I() {
    var p = A(), E = m(p);
    if (s = arguments, o = this, a = p, E) {
      if (i === void 0)
        return x(a);
      if (c)
        return clearTimeout(i), i = setTimeout(_, t), u(a);
    }
    return i === void 0 && (i = setTimeout(_, t)), l;
  }
  return I.cancel = y, I.flush = f, I;
}
function Te(e, t) {
  return me(e, t);
}
var le = {
  exports: {}
}, F = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Fe = v, Ae = Symbol.for("react.element"), Le = Symbol.for("react.fragment"), Ne = Object.prototype.hasOwnProperty, We = Fe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Me = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function oe(e, t, r) {
  var s, o = {}, n = null, l = null;
  r !== void 0 && (n = "" + r), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (l = t.ref);
  for (s in t) Ne.call(t, s) && !Me.hasOwnProperty(s) && (o[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) o[s] === void 0 && (o[s] = t[s]);
  return {
    $$typeof: Ae,
    type: e,
    key: n,
    ref: l,
    props: o,
    _owner: We.current
  };
}
F.Fragment = Le;
F.jsx = oe;
F.jsxs = oe;
le.exports = F;
var w = le.exports;
const {
  SvelteComponent: De,
  assign: J,
  binding_callbacks: X,
  check_outros: Ve,
  children: se,
  claim_element: ie,
  claim_space: Ue,
  component_subscribe: Y,
  compute_slots: Be,
  create_slot: He,
  detach: R,
  element: ce,
  empty: K,
  exclude_internal_props: Q,
  get_all_dirty_from_scope: qe,
  get_slot_changes: ze,
  group_outros: Ge,
  init: Je,
  insert_hydration: P,
  safe_not_equal: Xe,
  set_custom_element_data: ae,
  space: Ye,
  transition_in: j,
  transition_out: U,
  update_slot_base: Ke
} = window.__gradio__svelte__internal, {
  beforeUpdate: Qe,
  getContext: Ze,
  onDestroy: $e,
  setContext: et
} = window.__gradio__svelte__internal;
function Z(e) {
  let t, r;
  const s = (
    /*#slots*/
    e[7].default
  ), o = He(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ce("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = ie(n, "SVELTE-SLOT", {
        class: !0
      });
      var l = se(t);
      o && o.l(l), l.forEach(R), this.h();
    },
    h() {
      ae(t, "class", "svelte-1rt0kpf");
    },
    m(n, l) {
      P(n, t, l), o && o.m(t, null), e[9](t), r = !0;
    },
    p(n, l) {
      o && o.p && (!r || l & /*$$scope*/
      64) && Ke(
        o,
        s,
        n,
        /*$$scope*/
        n[6],
        r ? ze(
          s,
          /*$$scope*/
          n[6],
          l,
          null
        ) : qe(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      r || (j(o, n), r = !0);
    },
    o(n) {
      U(o, n), r = !1;
    },
    d(n) {
      n && R(t), o && o.d(n), e[9](null);
    }
  };
}
function tt(e) {
  let t, r, s, o, n = (
    /*$$slots*/
    e[4].default && Z(e)
  );
  return {
    c() {
      t = ce("react-portal-target"), r = Ye(), n && n.c(), s = K(), this.h();
    },
    l(l) {
      t = ie(l, "REACT-PORTAL-TARGET", {
        class: !0
      }), se(t).forEach(R), r = Ue(l), n && n.l(l), s = K(), this.h();
    },
    h() {
      ae(t, "class", "svelte-1rt0kpf");
    },
    m(l, i) {
      P(l, t, i), e[8](t), P(l, r, i), n && n.m(l, i), P(l, s, i), o = !0;
    },
    p(l, [i]) {
      /*$$slots*/
      l[4].default ? n ? (n.p(l, i), i & /*$$slots*/
      16 && j(n, 1)) : (n = Z(l), n.c(), j(n, 1), n.m(s.parentNode, s)) : n && (Ge(), U(n, 1, 1, () => {
        n = null;
      }), Ve());
    },
    i(l) {
      o || (j(n), o = !0);
    },
    o(l) {
      U(n), o = !1;
    },
    d(l) {
      l && (R(t), R(r), R(s)), e[8](null), n && n.d(l);
    }
  };
}
function $(e) {
  const {
    svelteInit: t,
    ...r
  } = e;
  return r;
}
function nt(e, t, r) {
  let s, o, {
    $$slots: n = {},
    $$scope: l
  } = t;
  const i = Be(n);
  let {
    svelteInit: a
  } = t;
  const C = O($(t)), h = O();
  Y(e, h, (f) => r(0, s = f));
  const c = O();
  Y(e, c, (f) => r(1, o = f));
  const g = [], u = Ze("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: d,
    subSlotIndex: m
  } = he() || {}, _ = a({
    parent: u,
    props: C,
    target: h,
    slot: c,
    slotKey: x,
    slotIndex: d,
    subSlotIndex: m,
    onDestroy(f) {
      g.push(f);
    }
  });
  et("$$ms-gr-react-wrapper", _), Qe(() => {
    C.set($(t));
  }), $e(() => {
    g.forEach((f) => f());
  });
  function b(f) {
    X[f ? "unshift" : "push"](() => {
      s = f, h.set(s);
    });
  }
  function y(f) {
    X[f ? "unshift" : "push"](() => {
      o = f, c.set(o);
    });
  }
  return e.$$set = (f) => {
    r(17, t = J(J({}, t), Q(f))), "svelteInit" in f && r(5, a = f.svelteInit), "$$scope" in f && r(6, l = f.$$scope);
  }, t = Q(t), [s, o, h, c, i, a, l, n, b, y];
}
class rt extends De {
  constructor(t) {
    super(), Je(this, t, nt, tt, Xe, {
      svelteInit: 5
    });
  }
}
const ee = window.ms_globals.rerender, L = window.ms_globals.tree;
function lt(e, t = {}) {
  function r(s) {
    const o = O(), n = new rt({
      ...s,
      props: {
        svelteInit(l) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: l.props,
            slot: l.slot,
            target: l.target,
            slotIndex: l.slotIndex,
            subSlotIndex: l.subSlotIndex,
            ignore: t.ignore,
            slotKey: l.slotKey,
            nodes: []
          }, a = l.parent ?? L;
          return a.nodes = [...a.nodes, i], ee({
            createPortal: D,
            node: L
          }), l.onDestroy(() => {
            a.nodes = a.nodes.filter((C) => C.svelteInstance !== o), ee({
              createPortal: D,
              node: L
            });
          }), i;
        },
        ...s.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(r);
    });
  });
}
const ot = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function st(e) {
  return e ? Object.keys(e).reduce((t, r) => {
    const s = e[r];
    return t[r] = it(r, s), t;
  }, {}) : {};
}
function it(e, t) {
  return typeof t == "number" && !ot.includes(e) ? t + "px" : t;
}
function B(e) {
  const t = [], r = e.cloneNode(!1);
  if (e._reactElement) {
    const o = v.Children.toArray(e._reactElement.props.children).map((n) => {
      if (v.isValidElement(n) && n.props.__slot__) {
        const {
          portals: l,
          clonedElement: i
        } = B(n.props.el);
        return v.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...v.Children.toArray(n.props.children), ...l]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(D(v.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), r)), {
      clonedElement: r,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: l,
      type: i,
      useCapture: a
    }) => {
      r.addEventListener(i, l, a);
    });
  });
  const s = Array.from(e.childNodes);
  for (let o = 0; o < s.length; o++) {
    const n = s[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: l,
        portals: i
      } = B(n);
      t.push(...i), r.appendChild(l);
    } else n.nodeType === 3 && r.appendChild(n.cloneNode());
  }
  return {
    clonedElement: r,
    portals: t
  };
}
function ct(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const S = ne(({
  slot: e,
  clone: t,
  className: r,
  style: s,
  observeAttributes: o
}, n) => {
  const l = W(), [i, a] = re([]), {
    forceClone: C
  } = pe(), h = C ? !0 : t;
  return M(() => {
    var x;
    if (!l.current || !e)
      return;
    let c = e;
    function g() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), ct(n, d), r && d.classList.add(...r.split(" ")), s) {
        const m = st(s);
        Object.keys(m).forEach((_) => {
          d.style[_] = m[_];
        });
      }
    }
    let u = null;
    if (h && window.MutationObserver) {
      let d = function() {
        var y, f, I;
        (y = l.current) != null && y.contains(c) && ((f = l.current) == null || f.removeChild(c));
        const {
          portals: _,
          clonedElement: b
        } = B(e);
        c = b, a(_), c.style.display = "contents", g(), (I = l.current) == null || I.appendChild(c);
      };
      d();
      const m = je(() => {
        d(), u == null || u.disconnect(), u == null || u.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      u = new window.MutationObserver(m), u.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (x = l.current) == null || x.appendChild(c);
    return () => {
      var d, m;
      c.style.display = "", (d = l.current) != null && d.contains(c) && ((m = l.current) == null || m.removeChild(c)), u == null || u.disconnect();
    };
  }, [e, h, r, s, n, o]), v.createElement("react-child", {
    ref: l,
    style: {
      display: "contents"
    }
  }, ...i);
});
function at(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ut(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !at(e))
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
function N(e, t) {
  return H(() => ut(e, t), [e, t]);
}
function dt({
  value: e,
  onValueChange: t
}) {
  const [r, s] = re(e), o = W(t);
  o.current = t;
  const n = W(r);
  return n.current = r, M(() => {
    o.current(r);
  }, [r]), M(() => {
    Te(e, n.current) || s(e);
  }, [e]), [r, s];
}
function ue(e, t, r) {
  const s = e.filter(Boolean);
  if (s.length !== 0)
    return s.map((o, n) => {
      var C;
      if (typeof o != "object")
        return t != null && t.fallback ? t.fallback(o) : o;
      const l = {
        ...o.props,
        key: ((C = o.props) == null ? void 0 : C.key) ?? (r ? `${r}-${n}` : `${n}`)
      };
      let i = l;
      Object.keys(o.slots).forEach((h) => {
        if (!o.slots[h] || !(o.slots[h] instanceof Element) && !o.slots[h].el)
          return;
        const c = h.split(".");
        c.forEach((_, b) => {
          i[_] || (i[_] = {}), b !== c.length - 1 && (i = l[_]);
        });
        const g = o.slots[h];
        let u, x, d = (t == null ? void 0 : t.clone) ?? !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? u = g : (u = g.el, x = g.callback, d = g.clone ?? d, m = g.forceClone ?? m), m = m ?? !!x, i[c[c.length - 1]] = u ? x ? (..._) => (x(c[c.length - 1], _), /* @__PURE__ */ w.jsx(T, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ w.jsx(S, {
            slot: u,
            clone: d
          })
        })) : /* @__PURE__ */ w.jsx(T, {
          forceClone: m,
          children: /* @__PURE__ */ w.jsx(S, {
            slot: u,
            clone: d
          })
        }) : i[c[c.length - 1]], i = l;
      });
      const a = (t == null ? void 0 : t.children) || "children";
      return o[a] ? l[a] = ue(o[a], t, `${n}`) : t != null && t.children && (l[a] = void 0, Reflect.deleteProperty(l, a)), l;
    });
}
function te(e, t) {
  return e ? /* @__PURE__ */ w.jsx(S, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ft({
  key: e,
  slots: t,
  targets: r
}, s) {
  return t[e] ? (...o) => r ? r.map((n, l) => /* @__PURE__ */ w.jsx(T, {
    params: o,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: te(n, {
      clone: !0,
      ...s
    })
  }, l)) : /* @__PURE__ */ w.jsx(T, {
    params: o,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: te(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  useItems: mt,
  withItemsContextProvider: ht,
  ItemHandler: gt
} = we("antd-auto-complete-options"), _t = ne(({
  children: e,
  ...t
}, r) => /* @__PURE__ */ w.jsx(ge.Provider, {
  value: H(() => ({
    ...t,
    elRef: r
  }), [t, r]),
  children: e
})), Ct = lt(ht(["options", "default"], ({
  slots: e,
  children: t,
  onValueChange: r,
  filterOption: s,
  onChange: o,
  options: n,
  getPopupContainer: l,
  dropdownRender: i,
  elRef: a,
  setSlotParams: C,
  ...h
}) => {
  const c = N(l), g = N(s), u = N(i), [x, d] = dt({
    onValueChange: r,
    value: h.value
  }), {
    items: m
  } = mt(), _ = m.options.length > 0 ? m.options : m.default;
  return /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [e.children ? null : /* @__PURE__ */ w.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ w.jsx(Ce, {
      ...h,
      value: x,
      ref: a,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ w.jsx(S, {
          slot: e["allowClear.clearIcon"]
        })
      } : h.allowClear,
      options: H(() => n || ue(_, {
        children: "options"
        // clone: true,
      }), [_, n]),
      onChange: (b, ...y) => {
        o == null || o(b, ...y), d(b);
      },
      notFoundContent: e.notFoundContent ? /* @__PURE__ */ w.jsx(S, {
        slot: e.notFoundContent
      }) : h.notFoundContent,
      filterOption: g || s,
      getPopupContainer: c,
      dropdownRender: e.dropdownRender ? ft({
        slots: e,
        setSlotParams: C,
        key: "dropdownRender"
      }, {
        clone: !0
      }) : u,
      children: e.children ? /* @__PURE__ */ w.jsxs(_t, {
        children: [/* @__PURE__ */ w.jsx("div", {
          style: {
            display: "none"
          },
          children: t
        }), /* @__PURE__ */ w.jsx(S, {
          slot: e.children
        })]
      }) : null
    })]
  });
}));
export {
  Ct as AutoComplete,
  Ct as default
};
