import { i as ie, a as A, r as le, g as ae, w as O } from "./Index-DjzKqpfi.js";
const y = window.ms_globals.React, te = window.ms_globals.React.forwardRef, ne = window.ms_globals.React.useRef, re = window.ms_globals.React.useState, oe = window.ms_globals.React.useEffect, se = window.ms_globals.React.createElement, j = window.ms_globals.ReactDOM.createPortal, ce = window.ms_globals.internalContext.useContextPropsContext, de = window.ms_globals.antd.Row, ue = window.ms_globals.antd.Col, fe = window.ms_globals.createItemsContext.createItemsContext;
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
var M = NaN, ge = /^[-+]0x[0-9a-f]+$/i, we = /^0b[01]+$/i, be = /^0o[0-7]+$/i, ye = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (ie(e))
    return M;
  if (A(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = A(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = he(e);
  var o = we.test(e);
  return o || be.test(e) ? ye(e.slice(2), o ? 2 : 8) : ge.test(e) ? M : +e;
}
var L = function() {
  return le.Date.now();
}, Ee = "Expected a function", xe = Math.max, Ce = Math.min;
function ve(e, t, o) {
  var i, s, n, r, l, d, p = 0, g = !1, a = !1, w = !0;
  if (typeof e != "function")
    throw new TypeError(Ee);
  t = U(t) || 0, A(o) && (g = !!o.leading, a = "maxWait" in o, n = a ? xe(U(o.maxWait) || 0, t) : n, w = "trailing" in o ? !!o.trailing : w);
  function m(u) {
    var b = i, R = s;
    return i = s = void 0, p = u, r = e.apply(R, b), r;
  }
  function E(u) {
    return p = u, l = setTimeout(h, t), g ? m(u) : r;
  }
  function f(u) {
    var b = u - d, R = u - p, F = t - b;
    return a ? Ce(F, n - R) : F;
  }
  function _(u) {
    var b = u - d, R = u - p;
    return d === void 0 || b >= t || b < 0 || a && R >= n;
  }
  function h() {
    var u = L();
    if (_(u))
      return x(u);
    l = setTimeout(h, f(u));
  }
  function x(u) {
    return l = void 0, w && i ? m(u) : (i = s = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), p = 0, i = d = s = l = void 0;
  }
  function c() {
    return l === void 0 ? r : x(L());
  }
  function v() {
    var u = L(), b = _(u);
    if (i = arguments, s = this, d = u, b) {
      if (l === void 0)
        return E(d);
      if (a)
        return clearTimeout(l), l = setTimeout(h, t), m(d);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return v.cancel = C, v.flush = c, v;
}
var X = {
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
var Ie = y, Re = Symbol.for("react.element"), Se = Symbol.for("react.fragment"), Oe = Object.prototype.hasOwnProperty, Te = Ie.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ke = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Y(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Oe.call(t, i) && !ke.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Re,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Te.current
  };
}
P.Fragment = Se;
P.jsx = Y;
P.jsxs = Y;
X.exports = P;
var S = X.exports;
const {
  SvelteComponent: Pe,
  assign: H,
  binding_callbacks: z,
  check_outros: Le,
  children: Q,
  claim_element: Z,
  claim_space: Ne,
  component_subscribe: B,
  compute_slots: je,
  create_slot: Ae,
  detach: I,
  element: $,
  empty: G,
  exclude_internal_props: K,
  get_all_dirty_from_scope: We,
  get_slot_changes: De,
  group_outros: Fe,
  init: Me,
  insert_hydration: T,
  safe_not_equal: Ue,
  set_custom_element_data: ee,
  space: He,
  transition_in: k,
  transition_out: W,
  update_slot_base: ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: Be,
  getContext: Ge,
  onDestroy: Ke,
  setContext: qe
} = window.__gradio__svelte__internal;
function q(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = Ae(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = $("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = Z(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Q(t);
      s && s.l(r), r.forEach(I), this.h();
    },
    h() {
      ee(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && ze(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? De(
          i,
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
      o || (k(s, n), o = !0);
    },
    o(n) {
      W(s, n), o = !1;
    },
    d(n) {
      n && I(t), s && s.d(n), e[9](null);
    }
  };
}
function Ve(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = $("react-portal-target"), o = He(), n && n.c(), i = G(), this.h();
    },
    l(r) {
      t = Z(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Q(t).forEach(I), o = Ne(r), n && n.l(r), i = G(), this.h();
    },
    h() {
      ee(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      T(r, t, l), e[8](t), T(r, o, l), n && n.m(r, l), T(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && k(n, 1)) : (n = q(r), n.c(), k(n, 1), n.m(i.parentNode, i)) : n && (Fe(), W(n, 1, 1, () => {
        n = null;
      }), Le());
    },
    i(r) {
      s || (k(n), s = !0);
    },
    o(r) {
      W(n), s = !1;
    },
    d(r) {
      r && (I(t), I(o), I(i)), e[8](null), n && n.d(r);
    }
  };
}
function V(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Je(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = je(n);
  let {
    svelteInit: d
  } = t;
  const p = O(V(t)), g = O();
  B(e, g, (c) => o(0, i = c));
  const a = O();
  B(e, a, (c) => o(1, s = c));
  const w = [], m = Ge("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _
  } = ae() || {}, h = d({
    parent: m,
    props: p,
    target: g,
    slot: a,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(c) {
      w.push(c);
    }
  });
  qe("$$ms-gr-react-wrapper", h), Be(() => {
    p.set(V(t));
  }), Ke(() => {
    w.forEach((c) => c());
  });
  function x(c) {
    z[c ? "unshift" : "push"](() => {
      i = c, g.set(i);
    });
  }
  function C(c) {
    z[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    o(17, t = H(H({}, t), K(c))), "svelteInit" in c && o(5, d = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = K(t), [i, s, g, a, l, d, r, n, x, C];
}
class Xe extends Pe {
  constructor(t) {
    super(), Me(this, t, Je, Ve, Ue, {
      svelteInit: 5
    });
  }
}
const J = window.ms_globals.rerender, N = window.ms_globals.tree;
function Ye(e, t = {}) {
  function o(i) {
    const s = O(), n = new Xe({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
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
          }, d = r.parent ?? N;
          return d.nodes = [...d.nodes, l], J({
            createPortal: j,
            node: N
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((p) => p.svelteInstance !== s), J({
              createPortal: j,
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
      i(o);
    });
  });
}
const Qe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ze(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = $e(o, i), t;
  }, {}) : {};
}
function $e(e, t) {
  return typeof t == "number" && !Qe.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = y.Children.toArray(e._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(j(y.cloneElement(e._reactElement, {
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
      type: l,
      useCapture: d
    }) => {
      o.addEventListener(l, r, d);
    });
  });
  const i = Array.from(e.childNodes);
  for (let s = 0; s < i.length; s++) {
    const n = i[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = D(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function et(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const tt = te(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = ne(), [l, d] = re([]), {
    forceClone: p
  } = ce(), g = p ? !0 : t;
  return oe(() => {
    var E;
    if (!r.current || !e)
      return;
    let a = e;
    function w() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), et(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = Ze(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var C, c, v;
        (C = r.current) != null && C.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: h,
          clonedElement: x
        } = D(e);
        a = x, d(h), a.style.display = "contents", w(), (v = r.current) == null || v.appendChild(a);
      };
      f();
      const _ = ve(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", w(), (E = r.current) == null || E.appendChild(a);
    return () => {
      var f, _;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((_ = r.current) == null || _.removeChild(a)), m == null || m.disconnect();
    };
  }, [e, g, o, i, n, s]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), {
  withItemsContextProvider: nt,
  useItems: rt,
  ItemHandler: st
} = fe("antd-grid-cols"), it = Ye(nt(["default"], ({
  children: e,
  ...t
}) => {
  const {
    items: {
      default: o
    }
  } = rt();
  return /* @__PURE__ */ S.jsxs(S.Fragment, {
    children: [/* @__PURE__ */ S.jsx("div", {
      style: {
        display: "none"
      },
      children: e
    }), /* @__PURE__ */ S.jsx(de, {
      ...t,
      children: o == null ? void 0 : o.map((i, s) => {
        if (!i)
          return;
        const {
          el: n,
          props: r
        } = i;
        return /* @__PURE__ */ se(ue, {
          ...r,
          key: s
        }, n && /* @__PURE__ */ S.jsx(tt, {
          slot: n
        }));
      })
    })]
  });
}));
export {
  it as Row,
  it as default
};
