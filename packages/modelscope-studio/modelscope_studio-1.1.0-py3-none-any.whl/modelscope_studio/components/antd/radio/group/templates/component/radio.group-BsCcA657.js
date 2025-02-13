import { i as ae, a as A, r as ue, g as de, w as O } from "./Index-DPdD3IEq.js";
const y = window.ms_globals.React, oe = window.ms_globals.React.forwardRef, se = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, ie = window.ms_globals.React.useEffect, ce = window.ms_globals.React.useMemo, N = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, D = window.ms_globals.internalContext.ContextPropsProvider, me = window.ms_globals.internalContext.FormItemContext, pe = window.ms_globals.antd.Radio, _e = window.ms_globals.createItemsContext.createItemsContext;
var he = /\s/;
function ge(e) {
  for (var t = e.length; t-- && he.test(e.charAt(t)); )
    ;
  return t;
}
var be = /^\s+/;
function we(e) {
  return e && e.slice(0, ge(e) + 1).replace(be, "");
}
var G = NaN, xe = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, Ce = /^0o[0-7]+$/i, ye = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (ae(e))
    return G;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var s = Ee.test(e);
  return s || Ce.test(e) ? ye(e.slice(2), s ? 2 : 8) : xe.test(e) ? G : +e;
}
var j = function() {
  return ue.Date.now();
}, ve = "Expected a function", Ie = Math.max, Re = Math.min;
function Se(e, t, s) {
  var l, o, n, r, i, a, b = 0, h = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(ve);
  t = U(t) || 0, A(s) && (h = !!s.leading, c = "maxWait" in s, n = c ? Ie(U(s.maxWait) || 0, t) : n, g = "trailing" in s ? !!s.trailing : g);
  function d(p) {
    var E = l, S = o;
    return l = o = void 0, b = p, r = e.apply(S, E), r;
  }
  function w(p) {
    return b = p, i = setTimeout(_, t), h ? d(p) : r;
  }
  function f(p) {
    var E = p - a, S = p - b, M = t - E;
    return c ? Re(M, n - S) : M;
  }
  function m(p) {
    var E = p - a, S = p - b;
    return a === void 0 || E >= t || E < 0 || c && S >= n;
  }
  function _() {
    var p = j();
    if (m(p))
      return x(p);
    i = setTimeout(_, f(p));
  }
  function x(p) {
    return i = void 0, g && l ? d(p) : (l = o = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), b = 0, l = a = o = i = void 0;
  }
  function u() {
    return i === void 0 ? r : x(j());
  }
  function I() {
    var p = j(), E = m(p);
    if (l = arguments, o = this, a = p, E) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(_, t), d(a);
    }
    return i === void 0 && (i = setTimeout(_, t)), r;
  }
  return I.cancel = v, I.flush = u, I;
}
var Q = {
  exports: {}
}, P = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = y, ke = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), Pe = Object.prototype.hasOwnProperty, je = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Z(e, t, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Pe.call(t, l) && !Le.hasOwnProperty(l) && (o[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) o[l] === void 0 && (o[l] = t[l]);
  return {
    $$typeof: ke,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: je.current
  };
}
P.Fragment = Te;
P.jsx = Z;
P.jsxs = Z;
Q.exports = P;
var C = Q.exports;
const {
  SvelteComponent: Ne,
  assign: B,
  binding_callbacks: H,
  check_outros: Ae,
  children: $,
  claim_element: ee,
  claim_space: We,
  component_subscribe: z,
  compute_slots: Fe,
  create_slot: Me,
  detach: R,
  element: te,
  empty: q,
  exclude_internal_props: V,
  get_all_dirty_from_scope: De,
  get_slot_changes: Ge,
  group_outros: Ue,
  init: Be,
  insert_hydration: k,
  safe_not_equal: He,
  set_custom_element_data: ne,
  space: ze,
  transition_in: T,
  transition_out: W,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function J(e) {
  let t, s;
  const l = (
    /*#slots*/
    e[7].default
  ), o = Me(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = te("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = ee(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = $(t);
      o && o.l(r), r.forEach(R), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && qe(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? Ge(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : De(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (T(o, n), s = !0);
    },
    o(n) {
      W(o, n), s = !1;
    },
    d(n) {
      n && R(t), o && o.d(n), e[9](null);
    }
  };
}
function Ke(e) {
  let t, s, l, o, n = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = te("react-portal-target"), s = ze(), n && n.c(), l = q(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(R), s = We(r), n && n.l(r), l = q(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      k(r, t, i), e[8](t), k(r, s, i), n && n.m(r, i), k(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = J(r), n.c(), T(n, 1), n.m(l.parentNode, l)) : n && (Ue(), W(n, 1, 1, () => {
        n = null;
      }), Ae());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      W(n), o = !1;
    },
    d(r) {
      r && (R(t), R(s), R(l)), e[8](null), n && n.d(r);
    }
  };
}
function X(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function Qe(e, t, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Fe(n);
  let {
    svelteInit: a
  } = t;
  const b = O(X(t)), h = O();
  z(e, h, (u) => s(0, l = u));
  const c = O();
  z(e, c, (u) => s(1, o = u));
  const g = [], d = Je("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m
  } = de() || {}, _ = a({
    parent: d,
    props: b,
    target: h,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(u) {
      g.push(u);
    }
  });
  Ye("$$ms-gr-react-wrapper", _), Ve(() => {
    b.set(X(t));
  }), Xe(() => {
    g.forEach((u) => u());
  });
  function x(u) {
    H[u ? "unshift" : "push"](() => {
      l = u, h.set(l);
    });
  }
  function v(u) {
    H[u ? "unshift" : "push"](() => {
      o = u, c.set(o);
    });
  }
  return e.$$set = (u) => {
    s(17, t = B(B({}, t), V(u))), "svelteInit" in u && s(5, a = u.svelteInit), "$$scope" in u && s(6, r = u.$$scope);
  }, t = V(t), [l, o, h, c, i, a, r, n, x, v];
}
class Ze extends Ne {
  constructor(t) {
    super(), Be(this, t, Qe, Ke, He, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, L = window.ms_globals.tree;
function $e(e, t = {}) {
  function s(l) {
    const o = O(), n = new Ze({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? L;
          return a.nodes = [...a.nodes, i], Y({
            createPortal: N,
            node: L
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((b) => b.svelteInstance !== o), Y({
              createPortal: N,
              node: L
            });
          }), i;
        },
        ...l.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(s);
    });
  });
}
const et = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function tt(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const l = e[s];
    return t[s] = nt(s, l), t;
  }, {}) : {};
}
function nt(e, t) {
  return typeof t == "number" && !et.includes(e) ? t + "px" : t;
}
function F(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = F(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(N(y.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      s.addEventListener(i, r, a);
    });
  });
  const l = Array.from(e.childNodes);
  for (let o = 0; o < l.length; o++) {
    const n = l[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = F(n);
      t.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function rt(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const K = oe(({
  slot: e,
  clone: t,
  className: s,
  style: l,
  observeAttributes: o
}, n) => {
  const r = se(), [i, a] = le([]), {
    forceClone: b
  } = fe(), h = b ? !0 : t;
  return ie(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function g() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), rt(n, f), s && f.classList.add(...s.split(" ")), l) {
        const m = tt(l);
        Object.keys(m).forEach((_) => {
          f.style[_] = m[_];
        });
      }
    }
    let d = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var v, u, I;
        (v = r.current) != null && v.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: _,
          clonedElement: x
        } = F(e);
        c = x, a(_), c.style.display = "contents", g(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const m = Se(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      d = new window.MutationObserver(m), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, h, s, l, n, o]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function re(e, t, s) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((o, n) => {
      var b;
      if (typeof o != "object")
        return o;
      const r = {
        ...o.props,
        key: ((b = o.props) == null ? void 0 : b.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(o.slots).forEach((h) => {
        if (!o.slots[h] || !(o.slots[h] instanceof Element) && !o.slots[h].el)
          return;
        const c = h.split(".");
        c.forEach((_, x) => {
          i[_] || (i[_] = {}), x !== c.length - 1 && (i = r[_]);
        });
        const g = o.slots[h];
        let d, w, f = !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? d = g : (d = g.el, w = g.callback, f = g.clone ?? f, m = g.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = d ? w ? (..._) => (w(c[c.length - 1], _), /* @__PURE__ */ C.jsx(D, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ C.jsx(K, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ C.jsx(D, {
          forceClone: m,
          children: /* @__PURE__ */ C.jsx(K, {
            slot: d,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = "children";
      return o[a] && (r[a] = re(o[a], t, `${n}`)), r;
    });
}
const {
  withItemsContextProvider: ot,
  useItems: st,
  ItemHandler: it
} = _e("antd-radio-group-options"), ct = $e(ot(["options"], ({
  onValueChange: e,
  onChange: t,
  elRef: s,
  options: l,
  children: o,
  ...n
}) => {
  const {
    items: {
      options: r
    }
  } = st();
  return /* @__PURE__ */ C.jsx(C.Fragment, {
    children: /* @__PURE__ */ C.jsx(pe.Group, {
      ...n,
      ref: s,
      options: ce(() => l || re(r), [r, l]),
      onChange: (i) => {
        t == null || t(i), e(i.target.value);
      },
      children: /* @__PURE__ */ C.jsx(me.Provider, {
        value: null,
        children: o
      })
    })
  });
}));
export {
  ct as RadioGroup,
  ct as default
};
