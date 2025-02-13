import { i as ie, a as W, r as le, g as ae, w as O } from "./Index-CYvAu79z.js";
const w = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, A = window.ms_globals.ReactDOM.createPortal, ce = window.ms_globals.internalContext.useContextPropsContext, de = window.ms_globals.antd.Card;
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
var U = NaN, _e = /^[-+]0x[0-9a-f]+$/i, he = /^0b[01]+$/i, ge = /^0o[0-7]+$/i, be = parseInt;
function z(e) {
  if (typeof e == "number")
    return e;
  if (ie(e))
    return U;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = pe(e);
  var o = he.test(e);
  return o || ge.test(e) ? be(e.slice(2), o ? 2 : 8) : _e.test(e) ? U : +e;
}
var P = function() {
  return le.Date.now();
}, ye = "Expected a function", Ee = Math.max, we = Math.min;
function ve(e, t, o) {
  var i, s, n, r, l, d, p = 0, g = !1, a = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = z(t) || 0, W(o) && (g = !!o.leading, a = "maxWait" in o, n = a ? Ee(z(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function m(u) {
    var y = i, R = s;
    return i = s = void 0, p = u, r = e.apply(R, y), r;
  }
  function v(u) {
    return p = u, l = setTimeout(h, t), g ? m(u) : r;
  }
  function f(u) {
    var y = u - d, R = u - p, F = t - y;
    return a ? we(F, n - R) : F;
  }
  function _(u) {
    var y = u - d, R = u - p;
    return d === void 0 || y >= t || y < 0 || a && R >= n;
  }
  function h() {
    var u = P();
    if (_(u))
      return x(u);
    l = setTimeout(h, f(u));
  }
  function x(u) {
    return l = void 0, b && i ? m(u) : (i = s = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), p = 0, i = d = s = l = void 0;
  }
  function c() {
    return l === void 0 ? r : x(P());
  }
  function I() {
    var u = P(), y = _(u);
    if (i = arguments, s = this, d = u, y) {
      if (l === void 0)
        return v(d);
      if (a)
        return clearTimeout(l), l = setTimeout(h, t), m(d);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return I.cancel = C, I.flush = c, I;
}
var Y = {
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
var xe = w, Ce = Symbol.for("react.element"), Ie = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, Re = xe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Oe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Q(e, t, o) {
  var i, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (i in t) Se.call(t, i) && !Oe.hasOwnProperty(i) && (s[i] = t[i]);
  if (e && e.defaultProps) for (i in t = e.defaultProps, t) s[i] === void 0 && (s[i] = t[i]);
  return {
    $$typeof: Ce,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Re.current
  };
}
L.Fragment = Ie;
L.jsx = Q;
L.jsxs = Q;
Y.exports = L;
var E = Y.exports;
const {
  SvelteComponent: Te,
  assign: B,
  binding_callbacks: G,
  check_outros: ke,
  children: Z,
  claim_element: $,
  claim_space: Le,
  component_subscribe: H,
  compute_slots: Pe,
  create_slot: je,
  detach: S,
  element: ee,
  empty: K,
  exclude_internal_props: q,
  get_all_dirty_from_scope: Ne,
  get_slot_changes: Ae,
  group_outros: We,
  init: Me,
  insert_hydration: T,
  safe_not_equal: De,
  set_custom_element_data: te,
  space: Fe,
  transition_in: k,
  transition_out: M,
  update_slot_base: Ue
} = window.__gradio__svelte__internal, {
  beforeUpdate: ze,
  getContext: Be,
  onDestroy: Ge,
  setContext: He
} = window.__gradio__svelte__internal;
function V(e) {
  let t, o;
  const i = (
    /*#slots*/
    e[7].default
  ), s = je(
    i,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ee("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = $(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = Z(t);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      T(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ue(
        s,
        i,
        n,
        /*$$scope*/
        n[6],
        o ? Ae(
          i,
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
      o || (k(s, n), o = !0);
    },
    o(n) {
      M(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function Ke(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && V(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), o = Fe(), n && n.c(), i = K(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(S), o = Le(r), n && n.l(r), i = K(), this.h();
    },
    h() {
      te(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      T(r, t, l), e[8](t), T(r, o, l), n && n.m(r, l), T(r, i, l), s = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && k(n, 1)) : (n = V(r), n.c(), k(n, 1), n.m(i.parentNode, i)) : n && (We(), M(n, 1, 1, () => {
        n = null;
      }), ke());
    },
    i(r) {
      s || (k(n), s = !0);
    },
    o(r) {
      M(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(i)), e[8](null), n && n.d(r);
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
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Pe(n);
  let {
    svelteInit: d
  } = t;
  const p = O(J(t)), g = O();
  H(e, g, (c) => o(0, i = c));
  const a = O();
  H(e, a, (c) => o(1, s = c));
  const b = [], m = Be("$$ms-gr-react-wrapper"), {
    slotKey: v,
    slotIndex: f,
    subSlotIndex: _
  } = ae() || {}, h = d({
    parent: m,
    props: p,
    target: g,
    slot: a,
    slotKey: v,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(c) {
      b.push(c);
    }
  });
  He("$$ms-gr-react-wrapper", h), ze(() => {
    p.set(J(t));
  }), Ge(() => {
    b.forEach((c) => c());
  });
  function x(c) {
    G[c ? "unshift" : "push"](() => {
      i = c, g.set(i);
    });
  }
  function C(c) {
    G[c ? "unshift" : "push"](() => {
      s = c, a.set(s);
    });
  }
  return e.$$set = (c) => {
    o(17, t = B(B({}, t), q(c))), "svelteInit" in c && o(5, d = c.svelteInit), "$$scope" in c && o(6, r = c.$$scope);
  }, t = q(t), [i, s, g, a, l, d, r, n, x, C];
}
class Ve extends Te {
  constructor(t) {
    super(), Me(this, t, qe, Ke, De, {
      svelteInit: 5
    });
  }
}
const X = window.ms_globals.rerender, j = window.ms_globals.tree;
function Je(e, t = {}) {
  function o(i) {
    const s = O(), n = new Ve({
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
          }, d = r.parent ?? j;
          return d.nodes = [...d.nodes, l], X({
            createPortal: A,
            node: j
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((p) => p.svelteInstance !== s), X({
              createPortal: A,
              node: j
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
const Xe = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function Ye(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const i = e[o];
    return t[o] = Qe(o, i), t;
  }, {}) : {};
}
function Qe(e, t) {
  return typeof t == "number" && !Xe.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = w.Children.toArray(e._reactElement.props.children).map((n) => {
      if (w.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = D(n.props.el);
        return w.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...w.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(A(w.cloneElement(e._reactElement, {
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
function Ze(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const N = ne(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = re(), [l, d] = oe([]), {
    forceClone: p
  } = ce(), g = p ? !0 : t;
  return se(() => {
    var v;
    if (!r.current || !e)
      return;
    let a = e;
    function b() {
      let f = a;
      if (a.tagName.toLowerCase() === "svelte-slot" && a.children.length === 1 && a.children[0] && (f = a.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Ze(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = Ye(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var C, c, I;
        (C = r.current) != null && C.contains(a) && ((c = r.current) == null || c.removeChild(a));
        const {
          portals: h,
          clonedElement: x
        } = D(e);
        a = x, d(h), a.style.display = "contents", b(), (I = r.current) == null || I.appendChild(a);
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
      a.style.display = "contents", b(), (v = r.current) == null || v.appendChild(a);
    return () => {
      var f, _;
      a.style.display = "", (f = r.current) != null && f.contains(a) && ((_ = r.current) == null || _.removeChild(a)), m == null || m.disconnect();
    };
  }, [e, g, o, i, n, s]), w.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Je(({
  slots: e,
  children: t,
  ...o
}) => /* @__PURE__ */ E.jsxs(E.Fragment, {
  children: [/* @__PURE__ */ E.jsx("div", {
    style: {
      display: "none"
    },
    children: t
  }), /* @__PURE__ */ E.jsx(de.Meta, {
    ...o,
    title: e.title ? /* @__PURE__ */ E.jsx(N, {
      slot: e.title
    }) : o.title,
    description: e.description ? /* @__PURE__ */ E.jsx(N, {
      slot: e.description
    }) : o.description,
    avatar: e.avatar ? /* @__PURE__ */ E.jsx(N, {
      slot: e.avatar
    }) : o.avatar
  })]
}));
export {
  et as CardMeta,
  et as default
};
