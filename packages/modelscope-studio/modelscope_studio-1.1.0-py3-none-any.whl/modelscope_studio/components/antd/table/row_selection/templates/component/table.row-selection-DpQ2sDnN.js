import { i as ae, a as W, r as de, g as ue, w as O } from "./Index-mFOXwmCG.js";
const E = window.ms_globals.React, se = window.ms_globals.React.forwardRef, le = window.ms_globals.React.useRef, ie = window.ms_globals.React.useState, ce = window.ms_globals.React.useEffect, A = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, F = window.ms_globals.internalContext.ContextPropsProvider, P = window.ms_globals.createItemsContext.createItemsContext;
var me = /\s/;
function pe(e) {
  for (var t = e.length; t-- && me.test(e.charAt(t)); )
    ;
  return t;
}
var _e = /^\s+/;
function he(e) {
  return e && e.slice(0, pe(e) + 1).replace(_e, "");
}
var U = NaN, ge = /^[-+]0x[0-9a-f]+$/i, be = /^0b[01]+$/i, we = /^0o[0-7]+$/i, xe = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (ae(e))
    return U;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = he(e);
  var s = be.test(e);
  return s || we.test(e) ? xe(e.slice(2), s ? 2 : 8) : ge.test(e) ? U : +e;
}
var j = function() {
  return de.Date.now();
}, Ce = "Expected a function", Ee = Math.max, Ie = Math.min;
function ye(e, t, s) {
  var l, o, n, r, i, a, b = 0, h = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = B(t) || 0, W(s) && (h = !!s.leading, c = "maxWait" in s, n = c ? Ee(B(s.maxWait) || 0, t) : n, g = "trailing" in s ? !!s.trailing : g);
  function u(p) {
    var C = l, S = o;
    return l = o = void 0, b = p, r = e.apply(S, C), r;
  }
  function w(p) {
    return b = p, i = setTimeout(_, t), h ? u(p) : r;
  }
  function f(p) {
    var C = p - a, S = p - b, M = t - C;
    return c ? Ie(M, n - S) : M;
  }
  function m(p) {
    var C = p - a, S = p - b;
    return a === void 0 || C >= t || C < 0 || c && S >= n;
  }
  function _() {
    var p = j();
    if (m(p))
      return x(p);
    i = setTimeout(_, f(p));
  }
  function x(p) {
    return i = void 0, g && l ? u(p) : (l = o = void 0, r);
  }
  function I() {
    i !== void 0 && clearTimeout(i), b = 0, l = a = o = i = void 0;
  }
  function d() {
    return i === void 0 ? r : x(j());
  }
  function y() {
    var p = j(), C = m(p);
    if (l = arguments, o = this, a = p, C) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(_, t), u(a);
    }
    return i === void 0 && (i = setTimeout(_, t)), r;
  }
  return y.cancel = I, y.flush = d, y;
}
var Z = {
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
var ve = E, Se = Symbol.for("react.element"), Re = Symbol.for("react.fragment"), Oe = Object.prototype.hasOwnProperty, ke = ve.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Te = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function $(e, t, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Oe.call(t, l) && !Te.hasOwnProperty(l) && (o[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) o[l] === void 0 && (o[l] = t[l]);
  return {
    $$typeof: Se,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: ke.current
  };
}
L.Fragment = Re;
L.jsx = $;
L.jsxs = $;
Z.exports = L;
var R = Z.exports;
const {
  SvelteComponent: Pe,
  assign: z,
  binding_callbacks: G,
  check_outros: Le,
  children: ee,
  claim_element: te,
  claim_space: je,
  component_subscribe: q,
  compute_slots: Ne,
  create_slot: Ae,
  detach: v,
  element: ne,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: We,
  get_slot_changes: He,
  group_outros: De,
  init: Me,
  insert_hydration: k,
  safe_not_equal: Fe,
  set_custom_element_data: re,
  space: Ue,
  transition_in: T,
  transition_out: H,
  update_slot_base: Be
} = window.__gradio__svelte__internal, {
  beforeUpdate: ze,
  getContext: Ge,
  onDestroy: qe,
  setContext: Ve
} = window.__gradio__svelte__internal;
function X(e) {
  let t, s;
  const l = (
    /*#slots*/
    e[7].default
  ), o = Ae(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ne("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = te(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ee(t);
      o && o.l(r), r.forEach(v), this.h();
    },
    h() {
      re(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Be(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? He(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : We(
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
      H(o, n), s = !1;
    },
    d(n) {
      n && v(t), o && o.d(n), e[9](null);
    }
  };
}
function Je(e) {
  let t, s, l, o, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = ne("react-portal-target"), s = Ue(), n && n.c(), l = V(), this.h();
    },
    l(r) {
      t = te(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ee(t).forEach(v), s = je(r), n && n.l(r), l = V(), this.h();
    },
    h() {
      re(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      k(r, t, i), e[8](t), k(r, s, i), n && n.m(r, i), k(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = X(r), n.c(), T(n, 1), n.m(l.parentNode, l)) : n && (De(), H(n, 1, 1, () => {
        n = null;
      }), Le());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      H(n), o = !1;
    },
    d(r) {
      r && (v(t), v(s), v(l)), e[8](null), n && n.d(r);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function Xe(e, t, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Ne(n);
  let {
    svelteInit: a
  } = t;
  const b = O(Y(t)), h = O();
  q(e, h, (d) => s(0, l = d));
  const c = O();
  q(e, c, (d) => s(1, o = d));
  const g = [], u = Ge("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m
  } = ue() || {}, _ = a({
    parent: u,
    props: b,
    target: h,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(d) {
      g.push(d);
    }
  });
  Ve("$$ms-gr-react-wrapper", _), ze(() => {
    b.set(Y(t));
  }), qe(() => {
    g.forEach((d) => d());
  });
  function x(d) {
    G[d ? "unshift" : "push"](() => {
      l = d, h.set(l);
    });
  }
  function I(d) {
    G[d ? "unshift" : "push"](() => {
      o = d, c.set(o);
    });
  }
  return e.$$set = (d) => {
    s(17, t = z(z({}, t), J(d))), "svelteInit" in d && s(5, a = d.svelteInit), "$$scope" in d && s(6, r = d.$$scope);
  }, t = J(t), [l, o, h, c, i, a, r, n, x, I];
}
class Ye extends Pe {
  constructor(t) {
    super(), Me(this, t, Xe, Je, Fe, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ke(e, t = {}) {
  function s(l) {
    const o = O(), n = new Ye({
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
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], K({
            createPortal: A,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((b) => b.svelteInstance !== o), K({
              createPortal: A,
              node: N
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
const Qe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ze(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const l = e[s];
    return t[s] = $e(s, l), t;
  }, {}) : {};
}
function $e(e, t) {
  return typeof t == "number" && !Qe.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(A(E.cloneElement(e._reactElement, {
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
      } = D(n);
      t.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function et(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Q = se(({
  slot: e,
  clone: t,
  className: s,
  style: l,
  observeAttributes: o
}, n) => {
  const r = le(), [i, a] = ie([]), {
    forceClone: b
  } = fe(), h = b ? !0 : t;
  return ce(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function g() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), et(n, f), s && f.classList.add(...s.split(" ")), l) {
        const m = Ze(l);
        Object.keys(m).forEach((_) => {
          f.style[_] = m[_];
        });
      }
    }
    let u = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var I, d, y;
        (I = r.current) != null && I.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: _,
          clonedElement: x
        } = D(e);
        c = x, a(_), c.style.display = "contents", g(), (y = r.current) == null || y.appendChild(c);
      };
      f();
      const m = ye(() => {
        f(), u == null || u.disconnect(), u == null || u.observe(e, {
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
      c.style.display = "contents", g(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), u == null || u.disconnect();
    };
  }, [e, h, s, l, n, o]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function oe(e, t, s) {
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
        let u, w, f = !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? u = g : (u = g.el, w = g.callback, f = g.clone ?? f, m = g.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = u ? w ? (..._) => (w(c[c.length - 1], _), /* @__PURE__ */ R.jsx(F, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ R.jsx(Q, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ R.jsx(F, {
          forceClone: m,
          children: /* @__PURE__ */ R.jsx(Q, {
            slot: u,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = "children";
      return o[a] && (r[a] = oe(o[a], t, `${n}`)), r;
    });
}
P("antd-table-columns");
const {
  useItems: tt,
  withItemsContextProvider: nt,
  ItemHandler: st
} = P("antd-table-row-selection-selections"), {
  useItems: lt,
  withItemsContextProvider: it,
  ItemHandler: rt
} = P("antd-table-row-selection");
P("antd-table-expandable");
const ct = Ke(nt(["selections"], (e) => {
  const {
    items: {
      selections: t
    }
  } = tt();
  return /* @__PURE__ */ R.jsx(rt, {
    ...e,
    itemProps: (s) => ({
      ...s,
      selections: t.length > 0 ? oe(t) : s.selections
    })
  });
}));
export {
  ct as TableRowSelection,
  ct as default
};
