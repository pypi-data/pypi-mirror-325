import { i as ie, a as W, r as le, g as ce, w as T } from "./Index-BQrwwoNN.js";
const E = window.ms_globals.React, re = window.ms_globals.React.forwardRef, oe = window.ms_globals.React.useRef, se = window.ms_globals.React.useState, Q = window.ms_globals.React.useEffect, A = window.ms_globals.ReactDOM.createPortal, ae = window.ms_globals.internalContext.useContextPropsContext, de = window.ms_globals.antd.notification;
var ue = /\s/;
function fe(e) {
  for (var t = e.length; t-- && ue.test(e.charAt(t)); )
    ;
  return t;
}
var me = /^\s+/;
function _e(e) {
  return e && e.slice(0, fe(e) + 1).replace(me, "");
}
var H = NaN, he = /^[-+]0x[0-9a-f]+$/i, ge = /^0b[01]+$/i, pe = /^0o[0-7]+$/i, be = parseInt;
function U(e) {
  if (typeof e == "number")
    return e;
  if (ie(e))
    return H;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = _e(e);
  var s = ge.test(e);
  return s || pe.test(e) ? be(e.slice(2), s ? 2 : 8) : he.test(e) ? H : +e;
}
var N = function() {
  return le.Date.now();
}, ye = "Expected a function", we = Math.max, Ee = Math.min;
function xe(e, t, s) {
  var i, o, n, r, l, d, h = 0, c = !1, a = !1, p = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = U(t) || 0, W(s) && (c = !!s.leading, a = "maxWait" in s, n = a ? we(U(s.maxWait) || 0, t) : n, p = "trailing" in s ? !!s.trailing : p);
  function f(m) {
    var y = i, R = o;
    return i = o = void 0, h = m, r = e.apply(R, y), r;
  }
  function x(m) {
    return h = m, l = setTimeout(b, t), c ? f(m) : r;
  }
  function _(m) {
    var y = m - d, R = m - h, M = t - y;
    return a ? Ee(M, n - R) : M;
  }
  function g(m) {
    var y = m - d, R = m - h;
    return d === void 0 || y >= t || y < 0 || a && R >= n;
  }
  function b() {
    var m = N();
    if (g(m))
      return v(m);
    l = setTimeout(b, _(m));
  }
  function v(m) {
    return l = void 0, p && i ? f(m) : (i = o = void 0, r);
  }
  function I() {
    l !== void 0 && clearTimeout(l), h = 0, i = d = o = l = void 0;
  }
  function u() {
    return l === void 0 ? r : v(N());
  }
  function C() {
    var m = N(), y = g(m);
    if (i = arguments, o = this, d = m, y) {
      if (l === void 0)
        return x(d);
      if (a)
        return clearTimeout(l), l = setTimeout(b, t), f(d);
    }
    return l === void 0 && (l = setTimeout(b, t)), r;
  }
  return C.cancel = I, C.flush = u, C;
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
var ve = E, Ie = Symbol.for("react.element"), Ce = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, Re = ve.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Oe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function V(e, t, s) {
  var i, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Se.call(t, i) && !Oe.hasOwnProperty(i) && (o[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) o[i] === void 0 && (o[i] = t[i]);
  return {
    $$typeof: Ie,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: Re.current
  };
}
L.Fragment = Ce;
L.jsx = V;
L.jsxs = V;
Z.exports = L;
var w = Z.exports;
const {
  SvelteComponent: Te,
  assign: z,
  binding_callbacks: B,
  check_outros: ke,
  children: $,
  claim_element: ee,
  claim_space: Pe,
  component_subscribe: G,
  compute_slots: Le,
  create_slot: Ne,
  detach: S,
  element: te,
  empty: q,
  exclude_internal_props: J,
  get_all_dirty_from_scope: je,
  get_slot_changes: Ae,
  group_outros: We,
  init: De,
  insert_hydration: k,
  safe_not_equal: Fe,
  set_custom_element_data: ne,
  space: Me,
  transition_in: P,
  transition_out: D,
  update_slot_base: He
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ue,
  getContext: ze,
  onDestroy: Be,
  setContext: Ge
} = window.__gradio__svelte__internal;
function X(e) {
  let t, s;
  const i = (
    /*#slots*/
    e[7].default
  ), o = Ne(
    i,
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
      64) && He(
        o,
        i,
        n,
        /*$$scope*/
        n[6],
        s ? Ae(
          i,
          /*$$scope*/
          n[6],
          r,
          null
        ) : je(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (P(o, n), s = !0);
    },
    o(n) {
      D(o, n), s = !1;
    },
    d(n) {
      n && S(t), o && o.d(n), e[9](null);
    }
  };
}
function qe(e) {
  let t, s, i, o, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = te("react-portal-target"), s = Me(), n && n.c(), i = q(), this.h();
    },
    l(r) {
      t = ee(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), $(t).forEach(S), s = Pe(r), n && n.l(r), i = q(), this.h();
    },
    h() {
      ne(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      k(r, t, l), e[8](t), k(r, s, l), n && n.m(r, l), k(r, i, l), o = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && P(n, 1)) : (n = X(r), n.c(), P(n, 1), n.m(i.parentNode, i)) : n && (We(), D(n, 1, 1, () => {
        n = null;
      }), ke());
    },
    i(r) {
      o || (P(n), o = !0);
    },
    o(r) {
      D(n), o = !1;
    },
    d(r) {
      r && (S(t), S(s), S(i)), e[8](null), n && n.d(r);
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
function Je(e, t, s) {
  let i, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Le(n);
  let {
    svelteInit: d
  } = t;
  const h = T(Y(t)), c = T();
  G(e, c, (u) => s(0, i = u));
  const a = T();
  G(e, a, (u) => s(1, o = u));
  const p = [], f = ze("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: _,
    subSlotIndex: g
  } = ce() || {}, b = d({
    parent: f,
    props: h,
    target: c,
    slot: a,
    slotKey: x,
    slotIndex: _,
    subSlotIndex: g,
    onDestroy(u) {
      p.push(u);
    }
  });
  Ge("$$ms-gr-react-wrapper", b), Ue(() => {
    h.set(Y(t));
  }), Be(() => {
    p.forEach((u) => u());
  });
  function v(u) {
    B[u ? "unshift" : "push"](() => {
      i = u, c.set(i);
    });
  }
  function I(u) {
    B[u ? "unshift" : "push"](() => {
      o = u, a.set(o);
    });
  }
  return e.$$set = (u) => {
    s(17, t = z(z({}, t), J(u))), "svelteInit" in u && s(5, d = u.svelteInit), "$$scope" in u && s(6, r = u.$$scope);
  }, t = J(t), [i, o, c, a, l, d, r, n, v, I];
}
class Xe extends Te {
  constructor(t) {
    super(), De(this, t, Je, qe, Fe, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, j = window.ms_globals.tree;
function Ye(e, t = {}) {
  function s(i) {
    const o = T(), n = new Xe({
      ...i,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
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
          }, d = r.parent ?? j;
          return d.nodes = [...d.nodes, l], K({
            createPortal: A,
            node: j
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((h) => h.svelteInstance !== o), K({
              createPortal: A,
              node: j
            });
          }), l;
        },
        ...i.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((i) => {
    window.ms_globals.initializePromise.then(() => {
      i(s);
    });
  });
}
const Ke = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Qe(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const i = e[s];
    return t[s] = Ze(s, i), t;
  }, {}) : {};
}
function Ze(e, t) {
  return typeof t == "number" && !Ke.includes(e) ? t + "px" : t;
}
function F(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = F(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
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
      type: l,
      useCapture: d
    }) => {
      s.addEventListener(l, r, d);
    });
  });
  const i = Array.from(e.childNodes);
  for (let o = 0; o < i.length; o++) {
    const n = i[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = F(n);
      t.push(...l), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: t
  };
}
function Ve(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const O = re(({
  slot: e,
  clone: t,
  className: s,
  style: i,
  observeAttributes: o
}, n) => {
  const r = oe(), [l, d] = se([]), {
    forceClone: h
  } = ae(), c = h ? !0 : t;
  return Q(() => {
    var x;
    if (!r.current || !e)
      return;
    let a = e;
    function p() {
      let _ = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (_ = a.children[0], _.tagName.toLowerCase() === "react-portal-target" && _.children[0] && (_ = _.children[0])), Ve(n, _), s && _.classList.add(...s.split(" ")), i) {
        const g = Qe(i);
        Object.keys(g).forEach((b) => {
          _.style[b] = g[b];
        });
      }
    }
    let f = null;
    if (c && window.MutationObserver) {
      let _ = function() {
        var I, u, C;
        (I = r.current) != null && I.contains(a) && ((u = r.current) == null || u.removeChild(a));
        const {
          portals: b,
          clonedElement: v
        } = F(e);
        a = v, d(b), a.style.display = "contents", p(), (C = r.current) == null || C.appendChild(a);
      };
      _();
      const g = xe(() => {
        _(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      f = new window.MutationObserver(g), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      a.style.display = "contents", p(), (x = r.current) == null || x.appendChild(a);
    return () => {
      var _, g;
      a.style.display = "", (_ = r.current) != null && _.contains(a) && ((g = r.current) == null || g.removeChild(a)), f == null || f.disconnect();
    };
  }, [e, c, s, i, n, o]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Ye(({
  slots: e,
  bottom: t,
  rtl: s,
  stack: i,
  top: o,
  children: n,
  visible: r,
  notificationKey: l,
  onClose: d,
  onVisible: h,
  ...c
}) => {
  const [a, p] = de.useNotification({
    bottom: t,
    rtl: s,
    stack: i,
    top: o
  });
  return Q(() => (r ? a.open({
    ...c,
    key: l,
    btn: e.btn ? /* @__PURE__ */ w.jsx(O, {
      slot: e.btn
    }) : c.btn,
    closeIcon: e.closeIcon ? /* @__PURE__ */ w.jsx(O, {
      slot: e.closeIcon
    }) : c.closeIcon,
    description: e.description ? /* @__PURE__ */ w.jsx(O, {
      slot: e.description
    }) : c.description,
    message: e.message ? /* @__PURE__ */ w.jsx(O, {
      slot: e.message
    }) : c.message,
    icon: e.icon ? /* @__PURE__ */ w.jsx(O, {
      slot: e.icon
    }) : c.icon,
    onClose(...f) {
      h == null || h(!1), d == null || d(...f);
    }
  }) : a.destroy(l), () => {
    a.destroy(l);
  }), [r, l, c.btn, c.closeIcon, c.className, c.description, c.duration, c.showProgress, c.pauseOnHover, c.icon, c.message, c.placement, c.style, c.role, c.props]), /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [n, p]
  });
});
export {
  et as Notification,
  et as default
};
