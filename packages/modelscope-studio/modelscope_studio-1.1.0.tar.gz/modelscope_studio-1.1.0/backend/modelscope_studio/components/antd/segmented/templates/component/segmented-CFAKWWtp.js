import { i as ae, a as A, r as de, g as ue, w as R } from "./Index-DgJyUO0J.js";
const C = window.ms_globals.React, oe = window.ms_globals.React.forwardRef, se = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, ie = window.ms_globals.React.useEffect, ce = window.ms_globals.React.useMemo, N = window.ms_globals.ReactDOM.createPortal, fe = window.ms_globals.internalContext.useContextPropsContext, F = window.ms_globals.internalContext.ContextPropsProvider, me = window.ms_globals.antd.Segmented, pe = window.ms_globals.createItemsContext.createItemsContext;
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
var U = NaN, we = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, xe = /^0o[0-7]+$/i, ye = parseInt;
function B(e) {
  if (typeof e == "number")
    return e;
  if (ae(e))
    return U;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = be(e);
  var s = Ee.test(e);
  return s || xe.test(e) ? ye(e.slice(2), s ? 2 : 8) : we.test(e) ? U : +e;
}
var j = function() {
  return de.Date.now();
}, Ce = "Expected a function", ve = Math.max, Ie = Math.min;
function Se(e, t, s) {
  var l, o, n, r, i, a, b = 0, h = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Ce);
  t = B(t) || 0, A(s) && (h = !!s.leading, c = "maxWait" in s, n = c ? ve(B(s.maxWait) || 0, t) : n, g = "trailing" in s ? !!s.trailing : g);
  function u(p) {
    var x = l, O = o;
    return l = o = void 0, b = p, r = e.apply(O, x), r;
  }
  function w(p) {
    return b = p, i = setTimeout(_, t), h ? u(p) : r;
  }
  function f(p) {
    var x = p - a, O = p - b, D = t - x;
    return c ? Ie(D, n - O) : D;
  }
  function m(p) {
    var x = p - a, O = p - b;
    return a === void 0 || x >= t || x < 0 || c && O >= n;
  }
  function _() {
    var p = j();
    if (m(p))
      return E(p);
    i = setTimeout(_, f(p));
  }
  function E(p) {
    return i = void 0, g && l ? u(p) : (l = o = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), b = 0, l = a = o = i = void 0;
  }
  function d() {
    return i === void 0 ? r : E(j());
  }
  function I() {
    var p = j(), x = m(p);
    if (l = arguments, o = this, a = p, x) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(_, t), u(a);
    }
    return i === void 0 && (i = setTimeout(_, t)), r;
  }
  return I.cancel = v, I.flush = d, I;
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
var Oe = C, Re = Symbol.for("react.element"), ke = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, Pe = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, je = {
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
    $$typeof: Re,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Pe.current
  };
}
P.Fragment = ke;
P.jsx = Z;
P.jsxs = Z;
Q.exports = P;
var y = Q.exports;
const {
  SvelteComponent: Le,
  assign: H,
  binding_callbacks: z,
  check_outros: Ne,
  children: $,
  claim_element: ee,
  claim_space: Ae,
  component_subscribe: G,
  compute_slots: We,
  create_slot: Me,
  detach: S,
  element: te,
  empty: q,
  exclude_internal_props: V,
  get_all_dirty_from_scope: De,
  get_slot_changes: Fe,
  group_outros: Ue,
  init: Be,
  insert_hydration: k,
  safe_not_equal: He,
  set_custom_element_data: ne,
  space: ze,
  transition_in: T,
  transition_out: W,
  update_slot_base: Ge
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
      o && o.l(r), r.forEach(S), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Ge(
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
      n && S(t), o && o.d(n), e[9](null);
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
      t = te("react-portal-target"), s = ze(), n && n.c(), l = q(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(S), s = Ae(r), n && n.l(r), l = q(), this.h();
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
      }), Ne());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      W(n), o = !1;
    },
    d(r) {
      r && (S(t), S(s), S(l)), e[8](null), n && n.d(r);
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
  const b = R(X(t)), h = R();
  G(e, h, (d) => s(0, l = d));
  const c = R();
  G(e, c, (d) => s(1, o = d));
  const g = [], u = Ve("$$ms-gr-react-wrapper"), {
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
  Xe("$$ms-gr-react-wrapper", _), qe(() => {
    b.set(X(t));
  }), Je(() => {
    g.forEach((d) => d());
  });
  function E(d) {
    z[d ? "unshift" : "push"](() => {
      l = d, h.set(l);
    });
  }
  function v(d) {
    z[d ? "unshift" : "push"](() => {
      o = d, c.set(o);
    });
  }
  return e.$$set = (d) => {
    s(17, t = H(H({}, t), V(d))), "svelteInit" in d && s(5, a = d.svelteInit), "$$scope" in d && s(6, r = d.$$scope);
  }, t = V(t), [l, o, h, c, i, a, r, n, E, v];
}
class Qe extends Le {
  constructor(t) {
    super(), Be(this, t, Ke, Ye, He, {
      svelteInit: 5
    });
  }
}
const Y = window.ms_globals.rerender, L = window.ms_globals.tree;
function Ze(e, t = {}) {
  function s(l) {
    const o = R(), n = new Qe({
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
    var w;
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
    let u = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var v, d, I;
        (v = r.current) != null && v.contains(c) && ((d = r.current) == null || d.removeChild(c));
        const {
          portals: _,
          clonedElement: E
        } = M(e);
        c = E, a(_), c.style.display = "contents", g(), (I = r.current) == null || I.appendChild(c);
      };
      f();
      const m = Se(() => {
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
        c.forEach((_, E) => {
          i[_] || (i[_] = {}), E !== c.length - 1 && (i = r[_]);
        });
        const g = o.slots[h];
        let u, w, f = !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? u = g : (u = g.el, w = g.callback, f = g.clone ?? f, m = g.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = u ? w ? (..._) => (w(c[c.length - 1], _), /* @__PURE__ */ y.jsx(F, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ y.jsx(K, {
            slot: u,
            clone: f
          })
        })) : /* @__PURE__ */ y.jsx(F, {
          forceClone: m,
          children: /* @__PURE__ */ y.jsx(K, {
            slot: u,
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
} = pe("antd-segmented-options"), it = Ze(rt(["options", "default"], ({
  options: e,
  onChange: t,
  onValueChange: s,
  children: l,
  ...o
}) => {
  const {
    items: n
  } = ot(), r = n.options.length > 0 ? n.options : n.default;
  return /* @__PURE__ */ y.jsxs(y.Fragment, {
    children: [/* @__PURE__ */ y.jsx("div", {
      style: {
        display: "none"
      },
      children: l
    }), /* @__PURE__ */ y.jsx(me, {
      ...o,
      onChange: (i) => {
        t == null || t(i), s(i);
      },
      options: ce(() => e || re(r), [e, r])
    })]
  });
}));
export {
  it as Segmented,
  it as default
};
