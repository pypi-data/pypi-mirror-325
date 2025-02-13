import { i as ae, a as A, r as ue, g as de, w as O } from "./Index-m_YUzKPc.js";
const C = window.ms_globals.React, oe = window.ms_globals.React.forwardRef, se = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, ie = window.ms_globals.React.useEffect, ce = window.ms_globals.React.useMemo, N = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, F = window.ms_globals.internalContext.ContextPropsProvider, me = window.ms_globals.antd.Checkbox, pe = window.ms_globals.createItemsContext.createItemsContext;
var _e = /\s/;
function he(e) {
  for (var t = e.length; t-- && _e.test(e.charAt(t)); )
    ;
  return t;
}
var ge = /^\s+/;
function be(e) {
  return e && e.slice(0, he(e) + 1).replace(ge, "");
}
var G = NaN, xe = /^[-+]0x[0-9a-f]+$/i, we = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, ye = parseInt;
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
  e = be(e);
  var s = we.test(e);
  return s || Ee.test(e) ? ye(e.slice(2), s ? 2 : 8) : xe.test(e) ? G : +e;
}
var j = function() {
  return ue.Date.now();
}, Ce = "Expected a function", ve = Math.max, Ie = Math.min;
function ke(e, t, s) {
  var l, o, n, r, i, a, b = 0, h = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = U(t) || 0, A(s) && (h = !!s.leading, c = "maxWait" in s, n = c ? ve(U(s.maxWait) || 0, t) : n, g = "trailing" in s ? !!s.trailing : g);
  function d(p) {
    var E = l, S = o;
    return l = o = void 0, b = p, r = e.apply(S, E), r;
  }
  function x(p) {
    return b = p, i = setTimeout(_, t), h ? d(p) : r;
  }
  function f(p) {
    var E = p - a, S = p - b, D = t - E;
    return c ? Ie(D, n - S) : D;
  }
  function m(p) {
    var E = p - a, S = p - b;
    return a === void 0 || E >= t || E < 0 || c && S >= n;
  }
  function _() {
    var p = j();
    if (m(p))
      return w(p);
    i = setTimeout(_, f(p));
  }
  function w(p) {
    return i = void 0, g && l ? d(p) : (l = o = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), b = 0, l = a = o = i = void 0;
  }
  function u() {
    return i === void 0 ? r : w(j());
  }
  function I() {
    var p = j(), E = m(p);
    if (l = arguments, o = this, a = p, E) {
      if (i === void 0)
        return x(a);
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
var Se = C, Oe = Symbol.for("react.element"), Re = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, Pe = Se.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, je = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Z(e, t, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) Te.call(t, l) && !je.hasOwnProperty(l) && (o[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) o[l] === void 0 && (o[l] = t[l]);
  return {
    $$typeof: Oe,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Pe.current
  };
}
P.Fragment = Re;
P.jsx = Z;
P.jsxs = Z;
Q.exports = P;
var y = Q.exports;
const {
  SvelteComponent: Le,
  assign: B,
  binding_callbacks: H,
  check_outros: Ne,
  children: $,
  claim_element: ee,
  claim_space: Ae,
  component_subscribe: z,
  compute_slots: We,
  create_slot: Me,
  detach: k,
  element: te,
  empty: q,
  exclude_internal_props: V,
  get_all_dirty_from_scope: De,
  get_slot_changes: Fe,
  group_outros: Ge,
  init: Ue,
  insert_hydration: R,
  safe_not_equal: Be,
  set_custom_element_data: ne,
  space: He,
  transition_in: T,
  transition_out: W,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: qe,
  getContext: Ve,
  onDestroy: Je,
  setContext: Xe
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
      o && o.l(r), r.forEach(k), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      R(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && ze(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? Fe(
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
      n && k(t), o && o.d(n), e[9](null);
    }
  };
}
function Ye(e) {
  let t, s, l, o, n = (
    /*$$slots*/
    e[4].default && J(e)
  );
  return {
    c() {
      t = te("react-portal-target"), s = He(), n && n.c(), l = q(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(k), s = Ae(r), n && n.l(r), l = q(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      R(r, t, i), e[8](t), R(r, s, i), n && n.m(r, i), R(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = J(r), n.c(), T(n, 1), n.m(l.parentNode, l)) : n && (Ge(), W(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      W(n), o = !1;
    },
    d(r) {
      r && (k(t), k(s), k(l)), e[8](null), n && n.d(r);
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
function Ke(e, t, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = We(n);
  let {
    svelteInit: a
  } = t;
  const b = O(X(t)), h = O();
  z(e, h, (u) => s(0, l = u));
  const c = O();
  z(e, c, (u) => s(1, o = u));
  const g = [], d = Ve("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: m
  } = de() || {}, _ = a({
    parent: d,
    props: b,
    target: h,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: m,
    onDestroy(u) {
      g.push(u);
    }
  });
  Xe("$$ms-gr-react-wrapper", _), qe(() => {
    b.set(X(t));
  }), Je(() => {
    g.forEach((u) => u());
  });
  function w(u) {
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
  }, t = V(t), [l, o, h, c, i, a, r, n, w, v];
}
class Qe extends Le {
  constructor(t) {
    super(), Ue(this, t, Ke, Ye, Be, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, L = window.ms_globals.tree;
function Ze(e, t = {}) {
  function s(l) {
    const o = O(), n = new Qe({
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
const $e = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function et(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const l = e[s];
    return t[s] = tt(s, l), t;
  }, {}) : {};
}
function tt(e, t) {
  return typeof t == "number" && !$e.includes(e) ? t + "px" : t;
}
function M(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = M(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...C.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(N(C.cloneElement(e._reactElement, {
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
      } = M(n);
      t.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function nt(e, t) {
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
    var x;
    if (!r.current || !e)
      return;
    let c = e;
    function g() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), nt(n, f), s && f.classList.add(...s.split(" ")), l) {
        const m = et(l);
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
          clonedElement: w
        } = M(e);
        c = w, a(_), c.style.display = "contents", g(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const m = ke(() => {
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
      c.style.display = "contents", g(), (x = r.current) == null || x.appendChild(c);
    return () => {
      var f, m;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, h, s, l, n, o]), C.createElement("react-child", {
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
        c.forEach((_, w) => {
          i[_] || (i[_] = {}), w !== c.length - 1 && (i = r[_]);
        });
        const g = o.slots[h];
        let d, x, f = !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? d = g : (d = g.el, x = g.callback, f = g.clone ?? f, m = g.forceClone ?? m), m = m ?? !!x, i[c[c.length - 1]] = d ? x ? (..._) => (x(c[c.length - 1], _), /* @__PURE__ */ y.jsx(F, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ y.jsx(K, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ y.jsx(F, {
          forceClone: m,
          children: /* @__PURE__ */ y.jsx(K, {
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
  withItemsContextProvider: rt,
  useItems: ot,
  ItemHandler: lt
} = pe("antd-checkbox-group-options"), it = Ze(rt(["default", "options"], ({
  onValueChange: e,
  onChange: t,
  elRef: s,
  options: l,
  children: o,
  ...n
}) => {
  const {
    items: r
  } = ot(), i = r.options ? r.options : r.default;
  return /* @__PURE__ */ y.jsxs(y.Fragment, {
    children: [/* @__PURE__ */ y.jsx("div", {
      style: {
        display: "none"
      },
      children: o
    }), /* @__PURE__ */ y.jsx(me.Group, {
      ...n,
      ref: s,
      options: ce(() => l || re(i), [i, l]),
      onChange: (a) => {
        t == null || t(a), e(a);
      }
    })]
  });
}));
export {
  it as CheckboxGroup,
  it as default
};
