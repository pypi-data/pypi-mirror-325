import { i as le, a as M, r as ae, g as ce, w as R } from "./Index-DxhWCSSM.js";
const w = window.ms_globals.React, re = window.ms_globals.React.forwardRef, oe = window.ms_globals.React.useRef, ie = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, D = window.ms_globals.ReactDOM.createPortal, ue = window.ms_globals.internalContext.useContextPropsContext, P = window.ms_globals.antd.Empty;
var de = /\s/;
function fe(e) {
  for (var t = e.length; t-- && de.test(e.charAt(t)); )
    ;
  return t;
}
var me = /^\s+/;
function _e(e) {
  return e && e.slice(0, fe(e) + 1).replace(me, "");
}
var G = NaN, pe = /^[-+]0x[0-9a-f]+$/i, ge = /^0b[01]+$/i, he = /^0o[0-7]+$/i, Ee = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (le(e))
    return G;
  if (M(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = M(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = _e(e);
  var o = ge.test(e);
  return o || he.test(e) ? Ee(e.slice(2), o ? 2 : 8) : pe.test(e) ? G : +e;
}
var L = function() {
  return ae.Date.now();
}, be = "Expected a function", we = Math.max, ye = Math.min;
function ve(e, t, o) {
  var s, i, n, r, l, u, _ = 0, h = !1, a = !1, E = !0;
  if (typeof e != "function")
    throw new TypeError(be);
  t = U(t) || 0, M(o) && (h = !!o.leading, a = "maxWait" in o, n = a ? we(U(o.maxWait) || 0, t) : n, E = "trailing" in o ? !!o.trailing : E);
  function m(d) {
    var b = s, S = i;
    return s = i = void 0, _ = d, r = e.apply(S, b), r;
  }
  function y(d) {
    return _ = d, l = setTimeout(g, t), h ? m(d) : r;
  }
  function f(d) {
    var b = d - u, S = d - _, F = t - b;
    return a ? ye(F, n - S) : F;
  }
  function p(d) {
    var b = d - u, S = d - _;
    return u === void 0 || b >= t || b < 0 || a && S >= n;
  }
  function g() {
    var d = L();
    if (p(d))
      return v(d);
    l = setTimeout(g, f(d));
  }
  function v(d) {
    return l = void 0, E && s ? m(d) : (s = i = void 0, r);
  }
  function x() {
    l !== void 0 && clearTimeout(l), _ = 0, s = u = i = l = void 0;
  }
  function c() {
    return l === void 0 ? r : v(L());
  }
  function I() {
    var d = L(), b = p(d);
    if (s = arguments, i = this, u = d, b) {
      if (l === void 0)
        return y(u);
      if (a)
        return clearTimeout(l), l = setTimeout(g, t), m(u);
    }
    return l === void 0 && (l = setTimeout(g, t)), r;
  }
  return I.cancel = x, I.flush = c, I;
}
var Q = {
  exports: {}
}, k = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var xe = w, Ie = Symbol.for("react.element"), Ce = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, Re = xe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Te = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Z(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Se.call(t, s) && !Te.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Ie,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Re.current
  };
}
k.Fragment = Ce;
k.jsx = Z;
k.jsxs = Z;
Q.exports = k;
var A = Q.exports;
const {
  SvelteComponent: Oe,
  assign: z,
  binding_callbacks: B,
  check_outros: ke,
  children: $,
  claim_element: ee,
  claim_space: Pe,
  component_subscribe: H,
  compute_slots: Le,
  create_slot: Ae,
  detach: C,
  element: te,
  empty: K,
  exclude_internal_props: q,
  get_all_dirty_from_scope: Ne,
  get_slot_changes: De,
  group_outros: Me,
  init: je,
  insert_hydration: T,
  safe_not_equal: We,
  set_custom_element_data: ne,
  space: Fe,
  transition_in: O,
  transition_out: j,
  update_slot_base: Ge
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ue,
  getContext: ze,
  onDestroy: Be,
  setContext: He
} = window.__gradio__svelte__internal;
function V(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Ae(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = te("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = ee(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = $(t);
      i && i.l(r), r.forEach(C), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && Ge(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? De(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ne(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (O(i, n), o = !0);
    },
    o(n) {
      j(i, n), o = !1;
    },
    d(n) {
      n && C(t), i && i.d(n), e[9](null);
    }
  };
}
function Ke(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && V(e)
  );
  return {
    c() {
      t = te("react-portal-target"), o = Fe(), n && n.c(), s = K(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(C), o = Pe(r), n && n.l(r), s = K(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      T(r, t, l), e[8](t), T(r, o, l), n && n.m(r, l), T(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && O(n, 1)) : (n = V(r), n.c(), O(n, 1), n.m(s.parentNode, s)) : n && (Me(), j(n, 1, 1, () => {
        n = null;
      }), ke());
    },
    i(r) {
      i || (O(n), i = !0);
    },
    o(r) {
      j(n), i = !1;
    },
    d(r) {
      r && (C(t), C(o), C(s)), e[8](null), n && n.d(r);
    }
  };
}
function J(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function qe(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Le(n);
  let {
    svelteInit: u
  } = t;
  const _ = R(J(t)), h = R();
  H(e, h, (c) => o(0, s = c));
  const a = R();
  H(e, a, (c) => o(1, i = c));
  const E = [], m = ze("$$ms-gr-react-wrapper"), {
    slotKey: y,
    slotIndex: f,
    subSlotIndex: p
  } = ce() || {}, g = u({
    parent: m,
    props: _,
    target: h,
    slot: a,
    slotKey: y,
    slotIndex: f,
    subSlotIndex: p,
    onDestroy(c) {
      E.push(c);
    }
  });
  He("$$ms-gr-react-wrapper", g), Ue(() => {
    _.set(J(t));
  }), Be(() => {
    E.forEach((c) => c());
  });
  function v(c) {
    B[c ? "unshift" : "push"](() => {
      s = c, h.set(s);
    });
  }
  function x(c) {
    B[c ? "unshift" : "push"](() => {
      i = c, a.set(i);
    });
  }
  return e.$$set = (c) => {
    o(17, t = z(z({}, t), q(c))), "svelteInit" in c && o(5, u = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = q(t), [s, i, h, a, l, u, r, n, v, x];
}
class Ve extends Oe {
  constructor(t) {
    super(), je(this, t, qe, Ke, We, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, N = window.ms_globals.tree;
function Je(e, t = {}) {
  function o(s) {
    const i = R(), n = new Ve({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? N;
          return u.nodes = [...u.nodes, l], X({
            createPortal: D,
            node: N
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== i), X({
              createPortal: D,
              node: N
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const Xe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ye(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = Qe(o, s), t;
  }, {}) : {};
}
function Qe(e, t) {
  return typeof t == "number" && !Xe.includes(e) ? t + "px" : t;
}
function W(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = w.Children.toArray(e._reactElement.props.children).map((n) => {
      if (w.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = W(n.props.el);
        return w.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...w.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(D(w.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = W(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function Ze(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const Y = re(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = oe(), [l, u] = ie([]), {
    forceClone: _
  } = ue(), h = _ ? !0 : t;
  return se(() => {
    var y;
    if (!r.current || !e)
      return;
    let a = e;
    function E() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Ze(n, f), o && f.classList.add(...o.split(" ")), s) {
        const p = Ye(s);
        Object.keys(p).forEach((g) => {
          f.style[g] = p[g];
        });
      }
    }
    let m = null;
    if (h && window.MutationObserver) {
      let f = function() {
        var x, c, I;
        (x = r.current) != null && x.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: g,
          clonedElement: v
        } = W(e);
        a = v, u(g), a.style.display = "contents", E(), (I = r.current) == null || I.appendChild(a);
      };
      f();
      const p = ve(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      m = new window.MutationObserver(p), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", E(), (y = r.current) == null || y.appendChild(a);
    return () => {
      var f, p;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((p = r.current) == null || p.removeChild(a)), m == null || m.disconnect();
    };
  }, [e, h, o, s, n, i]), w.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Je(({
  slots: e,
  styles: t,
  ...o
}) => {
  const s = () => {
    if (e.image)
      return /* @__PURE__ */ A.jsx(Y, {
        slot: e.image
      });
    switch (o.image) {
      case "PRESENTED_IMAGE_DEFAULT":
        return P.PRESENTED_IMAGE_DEFAULT;
      case "PRESENTED_IMAGE_SIMPLE":
        return P.PRESENTED_IMAGE_SIMPLE;
      default:
        return o.image;
    }
  };
  return /* @__PURE__ */ A.jsx(P, {
    ...o,
    description: e.description ? /* @__PURE__ */ A.jsx(Y, {
      slot: e.description
    }) : o.description,
    styles: {
      ...t,
      image: {
        display: "inline-block",
        ...t == null ? void 0 : t.image
      }
    },
    image: s()
  });
});
export {
  et as Empty,
  et as default
};
