import { i as ue, a as A, r as de, b as fe, g as me, w as k, c as _e } from "./Index-C0OX_egP.js";
const C = window.ms_globals.React, ae = window.ms_globals.React.forwardRef, N = window.ms_globals.React.useRef, ee = window.ms_globals.React.useState, M = window.ms_globals.React.useEffect, te = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, he = window.ms_globals.internalContext.useContextPropsContext, H = window.ms_globals.internalContext.ContextPropsProvider, pe = window.ms_globals.antd.Mentions, ge = window.ms_globals.createItemsContext.createItemsContext;
var be = /\s/;
function we(e) {
  for (var t = e.length; t-- && be.test(e.charAt(t)); )
    ;
  return t;
}
var ye = /^\s+/;
function Ee(e) {
  return e && e.slice(0, we(e) + 1).replace(ye, "");
}
var q = NaN, xe = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Ie = parseInt;
function z(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return q;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Ee(e);
  var o = Ce.test(e);
  return o || ve.test(e) ? Ie(e.slice(2), o ? 2 : 8) : xe.test(e) ? q : +e;
}
var j = function() {
  return de.Date.now();
}, Se = "Expected a function", Re = Math.max, ke = Math.min;
function Oe(e, t, o) {
  var l, s, n, r, i, a, h = 0, g = !1, c = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(Se);
  t = z(t) || 0, A(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Re(z(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function d(p) {
    var x = l, R = s;
    return l = s = void 0, h = p, r = e.apply(R, x), r;
  }
  function w(p) {
    return h = p, i = setTimeout(_, t), g ? d(p) : r;
  }
  function u(p) {
    var x = p - a, R = p - h, B = t - x;
    return c ? ke(B, n - R) : B;
  }
  function m(p) {
    var x = p - a, R = p - h;
    return a === void 0 || x >= t || x < 0 || c && R >= n;
  }
  function _() {
    var p = j();
    if (m(p))
      return y(p);
    i = setTimeout(_, u(p));
  }
  function y(p) {
    return i = void 0, b && l ? d(p) : (l = s = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), h = 0, l = a = s = i = void 0;
  }
  function f() {
    return i === void 0 ? r : y(j());
  }
  function I() {
    var p = j(), x = m(p);
    if (l = arguments, s = this, a = p, x) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(_, t), d(a);
    }
    return i === void 0 && (i = setTimeout(_, t)), r;
  }
  return I.cancel = v, I.flush = f, I;
}
function Pe(e, t) {
  return fe(e, t);
}
var ne = {
  exports: {}
}, T = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Te = C, je = Symbol.for("react.element"), Fe = Symbol.for("react.fragment"), Le = Object.prototype.hasOwnProperty, Ne = Te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Me = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, t, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Le.call(t, l) && !Me.hasOwnProperty(l) && (s[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) s[l] === void 0 && (s[l] = t[l]);
  return {
    $$typeof: je,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Ne.current
  };
}
T.Fragment = Fe;
T.jsx = re;
T.jsxs = re;
ne.exports = T;
var E = ne.exports;
const {
  SvelteComponent: We,
  assign: G,
  binding_callbacks: J,
  check_outros: Ae,
  children: se,
  claim_element: oe,
  claim_space: De,
  component_subscribe: X,
  compute_slots: Ve,
  create_slot: Ue,
  detach: S,
  element: le,
  empty: Y,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Be,
  get_slot_changes: He,
  group_outros: qe,
  init: ze,
  insert_hydration: O,
  safe_not_equal: Ge,
  set_custom_element_data: ie,
  space: Je,
  transition_in: P,
  transition_out: D,
  update_slot_base: Xe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ye,
  getContext: Ke,
  onDestroy: Qe,
  setContext: Ze
} = window.__gradio__svelte__internal;
function Q(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = Ue(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = le("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = oe(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = se(t);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Xe(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? He(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Be(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (P(s, n), o = !0);
    },
    o(n) {
      D(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function $e(e) {
  let t, o, l, s, n = (
    /*$$slots*/
    e[4].default && Q(e)
  );
  return {
    c() {
      t = le("react-portal-target"), o = Je(), n && n.c(), l = Y(), this.h();
    },
    l(r) {
      t = oe(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), se(t).forEach(S), o = De(r), n && n.l(r), l = Y(), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, t, i), e[8](t), O(r, o, i), n && n.m(r, i), O(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && P(n, 1)) : (n = Q(r), n.c(), P(n, 1), n.m(l.parentNode, l)) : n && (qe(), D(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      s || (P(n), s = !0);
    },
    o(r) {
      D(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(l)), e[8](null), n && n.d(r);
    }
  };
}
function Z(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function et(e, t, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Ve(n);
  let {
    svelteInit: a
  } = t;
  const h = k(Z(t)), g = k();
  X(e, g, (f) => o(0, l = f));
  const c = k();
  X(e, c, (f) => o(1, s = f));
  const b = [], d = Ke("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: u,
    subSlotIndex: m
  } = me() || {}, _ = a({
    parent: d,
    props: h,
    target: g,
    slot: c,
    slotKey: w,
    slotIndex: u,
    subSlotIndex: m,
    onDestroy(f) {
      b.push(f);
    }
  });
  Ze("$$ms-gr-react-wrapper", _), Ye(() => {
    h.set(Z(t));
  }), Qe(() => {
    b.forEach((f) => f());
  });
  function y(f) {
    J[f ? "unshift" : "push"](() => {
      l = f, g.set(l);
    });
  }
  function v(f) {
    J[f ? "unshift" : "push"](() => {
      s = f, c.set(s);
    });
  }
  return e.$$set = (f) => {
    o(17, t = G(G({}, t), K(f))), "svelteInit" in f && o(5, a = f.svelteInit), "$$scope" in f && o(6, r = f.$$scope);
  }, t = K(t), [l, s, g, c, i, a, r, n, y, v];
}
class tt extends We {
  constructor(t) {
    super(), ze(this, t, et, $e, Ge, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, F = window.ms_globals.tree;
function nt(e, t = {}) {
  function o(l) {
    const s = k(), n = new tt({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? F;
          return a.nodes = [...a.nodes, i], $({
            createPortal: W,
            node: F
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((h) => h.svelteInstance !== s), $({
              createPortal: W,
              node: F
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
const rt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function st(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return t[o] = ot(o, l), t;
  }, {}) : {};
}
function ot(e, t) {
  return typeof t == "number" && !rt.includes(e) ? t + "px" : t;
}
function V(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = V(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...C.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(W(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      o.addEventListener(i, r, a);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = V(n);
      t.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function lt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const U = ae(({
  slot: e,
  clone: t,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = N(), [i, a] = ee([]), {
    forceClone: h
  } = he(), g = h ? !0 : t;
  return M(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function b() {
      let u = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (u = c.children[0], u.tagName.toLowerCase() === "react-portal-target" && u.children[0] && (u = u.children[0])), lt(n, u), o && u.classList.add(...o.split(" ")), l) {
        const m = st(l);
        Object.keys(m).forEach((_) => {
          u.style[_] = m[_];
        });
      }
    }
    let d = null;
    if (g && window.MutationObserver) {
      let u = function() {
        var v, f, I;
        (v = r.current) != null && v.contains(c) && ((f = r.current) == null || f.removeChild(c));
        const {
          portals: _,
          clonedElement: y
        } = V(e);
        c = y, a(_), c.style.display = "contents", b(), (I = r.current) == null || I.appendChild(c);
      };
      u();
      const m = Oe(() => {
        u(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      d = new window.MutationObserver(m), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var u, m;
      c.style.display = "", (u = r.current) != null && u.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, g, o, l, n, s]), C.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function it(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function ct(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !it(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function L(e, t) {
  return te(() => ct(e, t), [e, t]);
}
function at({
  value: e,
  onValueChange: t
}) {
  const [o, l] = ee(e), s = N(t);
  s.current = t;
  const n = N(o);
  return n.current = o, M(() => {
    s.current(o);
  }, [o]), M(() => {
    Pe(e, n.current) || l(e);
  }, [e]), [o, l];
}
function ce(e, t, o) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((s, n) => {
      var h;
      if (typeof s != "object")
        return t != null && t.fallback ? t.fallback(s) : s;
      const r = {
        ...s.props,
        key: ((h = s.props) == null ? void 0 : h.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(s.slots).forEach((g) => {
        if (!s.slots[g] || !(s.slots[g] instanceof Element) && !s.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((_, y) => {
          i[_] || (i[_] = {}), y !== c.length - 1 && (i = r[_]);
        });
        const b = s.slots[g];
        let d, w, u = (t == null ? void 0 : t.clone) ?? !1, m = t == null ? void 0 : t.forceClone;
        b instanceof Element ? d = b : (d = b.el, w = b.callback, u = b.clone ?? u, m = b.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = d ? w ? (..._) => (w(c[c.length - 1], _), /* @__PURE__ */ E.jsx(H, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ E.jsx(U, {
            slot: d,
            clone: u
          })
        })) : /* @__PURE__ */ E.jsx(H, {
          forceClone: m,
          children: /* @__PURE__ */ E.jsx(U, {
            slot: d,
            clone: u
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = (t == null ? void 0 : t.children) || "children";
      return s[a] ? r[a] = ce(s[a], t, `${n}`) : t != null && t.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
const {
  useItems: ut,
  withItemsContextProvider: dt,
  ItemHandler: mt
} = ge("antd-mentions-options"), _t = nt(dt(["options", "default"], ({
  slots: e,
  children: t,
  onValueChange: o,
  filterOption: l,
  onChange: s,
  options: n,
  validateSearch: r,
  getPopupContainer: i,
  elRef: a,
  ...h
}) => {
  const g = L(i), c = L(l), b = L(r), [d, w] = at({
    onValueChange: o,
    value: h.value
  }), {
    items: u
  } = ut(), m = u.options.length > 0 ? u.options : u.default;
  return /* @__PURE__ */ E.jsxs(E.Fragment, {
    children: [/* @__PURE__ */ E.jsx("div", {
      style: {
        display: "none"
      },
      children: t
    }), /* @__PURE__ */ E.jsx(pe, {
      ...h,
      ref: a,
      value: d,
      options: te(() => n || ce(m, {
        clone: !0
      }), [m, n]),
      onChange: (_, ...y) => {
        s == null || s(_, ...y), w(_);
      },
      validateSearch: b,
      notFoundContent: e.notFoundContent ? /* @__PURE__ */ E.jsx(U, {
        slot: e.notFoundContent
      }) : h.notFoundContent,
      filterOption: c || l,
      getPopupContainer: g
    })]
  });
}));
export {
  _t as Mentions,
  _t as default
};
