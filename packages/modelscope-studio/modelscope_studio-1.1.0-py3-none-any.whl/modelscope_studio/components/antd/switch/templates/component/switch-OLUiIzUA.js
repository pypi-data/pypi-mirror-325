import { i as ie, a as A, r as le, g as ce, w as R } from "./Index-CIsC3NLP.js";
const y = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, j = window.ms_globals.ReactDOM.createPortal, ae = window.ms_globals.internalContext.useContextPropsContext, de = window.ms_globals.antd.Switch;
var ue = /\s/;
function fe(e) {
  for (var t = e.length; t-- && ue.test(e.charAt(t)); )
    ;
  return t;
}
var me = /^\s+/;
function pe(e) {
  return e && e.slice(0, fe(e) + 1).replace(me, "");
}
var M = NaN, _e = /^[-+]0x[0-9a-f]+$/i, he = /^0b[01]+$/i, ge = /^0o[0-7]+$/i, be = parseInt;
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
  e = pe(e);
  var s = he.test(e);
  return s || ge.test(e) ? be(e.slice(2), s ? 2 : 8) : _e.test(e) ? M : +e;
}
var P = function() {
  return le.Date.now();
}, we = "Expected a function", ye = Math.max, Ee = Math.min;
function Ce(e, t, s) {
  var i, o, n, r, l, d, p = 0, g = !1, c = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(we);
  t = U(t) || 0, A(s) && (g = !!s.leading, c = "maxWait" in s, n = c ? ye(U(s.maxWait) || 0, t) : n, b = "trailing" in s ? !!s.trailing : b);
  function m(u) {
    var w = i, k = o;
    return i = o = void 0, p = u, r = e.apply(k, w), r;
  }
  function E(u) {
    return p = u, l = setTimeout(h, t), g ? m(u) : r;
  }
  function f(u) {
    var w = u - d, k = u - p, F = t - w;
    return c ? Ee(F, n - k) : F;
  }
  function _(u) {
    var w = u - d, k = u - p;
    return d === void 0 || w >= t || w < 0 || c && k >= n;
  }
  function h() {
    var u = P();
    if (_(u))
      return C(u);
    l = setTimeout(h, f(u));
  }
  function C(u) {
    return l = void 0, b && i ? m(u) : (i = o = void 0, r);
  }
  function x() {
    l !== void 0 && clearTimeout(l), p = 0, i = d = o = l = void 0;
  }
  function a() {
    return l === void 0 ? r : C(P());
  }
  function v() {
    var u = P(), w = _(u);
    if (i = arguments, o = this, d = u, w) {
      if (l === void 0)
        return E(d);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(d);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return v.cancel = x, v.flush = a, v;
}
var Q = {
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
var xe = y, ve = Symbol.for("react.element"), Ie = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, ke = xe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Re = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Z(e, t, s) {
  var i, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Se.call(t, i) && !Re.hasOwnProperty(i) && (o[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) o[i] === void 0 && (o[i] = t[i]);
  return {
    $$typeof: ve,
    type: e,
    key: n,
    ref: r,
    props: o,
    _owner: ke.current
  };
}
L.Fragment = Ie;
L.jsx = Z;
L.jsxs = Z;
Q.exports = L;
var I = Q.exports;
const {
  SvelteComponent: Oe,
  assign: z,
  binding_callbacks: B,
  check_outros: Te,
  children: V,
  claim_element: $,
  claim_space: Le,
  component_subscribe: G,
  compute_slots: Pe,
  create_slot: Ne,
  detach: S,
  element: ee,
  empty: H,
  exclude_internal_props: K,
  get_all_dirty_from_scope: je,
  get_slot_changes: Ae,
  group_outros: We,
  init: De,
  insert_hydration: O,
  safe_not_equal: Fe,
  set_custom_element_data: te,
  space: Me,
  transition_in: T,
  transition_out: W,
  update_slot_base: Ue
} = window.__gradio__svelte__internal, {
  beforeUpdate: ze,
  getContext: Be,
  onDestroy: Ge,
  setContext: He
} = window.__gradio__svelte__internal;
function q(e) {
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
      t = ee("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = V(t);
      o && o.l(r), r.forEach(S), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), o && o.m(t, null), e[9](t), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Ue(
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
function Ke(e) {
  let t, s, i, o, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), s = Me(), n && n.c(), i = H(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), V(t).forEach(S), s = Le(r), n && n.l(r), i = H(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      O(r, t, l), e[8](t), O(r, s, l), n && n.m(r, l), O(r, i, l), o = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && T(n, 1)) : (n = q(r), n.c(), T(n, 1), n.m(i.parentNode, i)) : n && (We(), W(n, 1, 1, () => {
        n = null;
      }), Te());
    },
    i(r) {
      o || (T(n), o = !0);
    },
    o(r) {
      W(n), o = !1;
    },
    d(r) {
      r && (S(t), S(s), S(i)), e[8](null), n && n.d(r);
    }
  };
}
function J(e) {
  const {
    svelteInit: t,
    ...s
  } = e;
  return s;
}
function qe(e, t, s) {
  let i, o, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Pe(n);
  let {
    svelteInit: d
  } = t;
  const p = R(J(t)), g = R();
  G(e, g, (a) => s(0, i = a));
  const c = R();
  G(e, c, (a) => s(1, o = a));
  const b = [], m = Be("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _
  } = ce() || {}, h = d({
    parent: m,
    props: p,
    target: g,
    slot: c,
    slotKey: E,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(a) {
      b.push(a);
    }
  });
  He("$$ms-gr-react-wrapper", h), ze(() => {
    p.set(J(t));
  }), Ge(() => {
    b.forEach((a) => a());
  });
  function C(a) {
    B[a ? "unshift" : "push"](() => {
      i = a, g.set(i);
    });
  }
  function x(a) {
    B[a ? "unshift" : "push"](() => {
      o = a, c.set(o);
    });
  }
  return e.$$set = (a) => {
    s(17, t = z(z({}, t), K(a))), "svelteInit" in a && s(5, d = a.svelteInit), "$$scope" in a && s(6, r = a.$$scope);
  }, t = K(t), [i, o, g, c, l, d, r, n, C, x];
}
class Je extends Oe {
  constructor(t) {
    super(), De(this, t, qe, Ke, Fe, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, N = window.ms_globals.tree;
function Xe(e, t = {}) {
  function s(i) {
    const o = R(), n = new Je({
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
          }, d = r.parent ?? N;
          return d.nodes = [...d.nodes, l], X({
            createPortal: j,
            node: N
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((p) => p.svelteInstance !== o), X({
              createPortal: j,
              node: N
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
const Ye = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Qe(e) {
  return e ? Object.keys(e).reduce((t, s) => {
    const i = e[s];
    return t[s] = Ze(s, i), t;
  }, {}) : {};
}
function Ze(e, t) {
  return typeof t == "number" && !Ye.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], s = e.cloneNode(!1);
  if (e._reactElement) {
    const o = y.Children.toArray(e._reactElement.props.children).map((n) => {
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
    return o.originalChildren = e._reactElement.props.children, t.push(j(y.cloneElement(e._reactElement, {
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
      } = D(n);
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
const Y = ne(({
  slot: e,
  clone: t,
  className: s,
  style: i,
  observeAttributes: o
}, n) => {
  const r = re(), [l, d] = oe([]), {
    forceClone: p
  } = ae(), g = p ? !0 : t;
  return se(() => {
    var E;
    if (!r.current || !e)
      return;
    let c = e;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Ve(n, f), s && f.classList.add(...s.split(" ")), i) {
        const _ = Qe(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var x, a, v;
        (x = r.current) != null && x.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: C
        } = D(e);
        c = C, d(h), c.style.display = "contents", b(), (v = r.current) == null || v.appendChild(c);
      };
      f();
      const _ = Ce(() => {
        f(), m == null || m.disconnect(), m == null || m.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      m = new window.MutationObserver(_), m.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", b(), (E = r.current) == null || E.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, s, i, n, o]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Xe(({
  slots: e,
  children: t,
  onValueChange: s,
  onChange: i,
  ...o
}) => /* @__PURE__ */ I.jsxs(I.Fragment, {
  children: [/* @__PURE__ */ I.jsx("div", {
    style: {
      display: "none"
    },
    children: t
  }), /* @__PURE__ */ I.jsx(de, {
    ...o,
    onChange: (n, ...r) => {
      s == null || s(n), i == null || i(n, ...r);
    },
    checkedChildren: e.checkedChildren ? /* @__PURE__ */ I.jsx(Y, {
      slot: e.checkedChildren
    }) : o.checkedChildren,
    unCheckedChildren: e.unCheckedChildren ? /* @__PURE__ */ I.jsx(Y, {
      slot: e.unCheckedChildren
    }) : o.unCheckedChildren
  })]
}));
export {
  et as Switch,
  et as default
};
