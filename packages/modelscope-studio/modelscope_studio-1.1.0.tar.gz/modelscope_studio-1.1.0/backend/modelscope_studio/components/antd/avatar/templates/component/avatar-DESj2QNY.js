import { i as ie, a as j, r as le, g as ce, w as O } from "./Index-mAqmeBNI.js";
const E = window.ms_globals.React, ne = window.ms_globals.React.forwardRef, re = window.ms_globals.React.useRef, oe = window.ms_globals.React.useState, se = window.ms_globals.React.useEffect, N = window.ms_globals.ReactDOM.createPortal, ae = window.ms_globals.internalContext.useContextPropsContext, ue = window.ms_globals.antd.Avatar;
var de = /\s/;
function fe(e) {
  for (var t = e.length; t-- && de.test(e.charAt(t)); )
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
  if (j(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = j(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = pe(e);
  var o = he.test(e);
  return o || ge.test(e) ? be(e.slice(2), o ? 2 : 8) : _e.test(e) ? M : +e;
}
var P = function() {
  return le.Date.now();
}, ye = "Expected a function", Ee = Math.max, we = Math.min;
function ve(e, t, o) {
  var i, s, n, r, l, u, p = 0, g = !1, c = !1, b = !0;
  if (typeof e != "function")
    throw new TypeError(ye);
  t = U(t) || 0, j(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Ee(U(o.maxWait) || 0, t) : n, b = "trailing" in o ? !!o.trailing : b);
  function m(d) {
    var y = i, R = s;
    return i = s = void 0, p = d, r = e.apply(R, y), r;
  }
  function w(d) {
    return p = d, l = setTimeout(h, t), g ? m(d) : r;
  }
  function f(d) {
    var y = d - u, R = d - p, F = t - y;
    return c ? we(F, n - R) : F;
  }
  function _(d) {
    var y = d - u, R = d - p;
    return u === void 0 || y >= t || y < 0 || c && R >= n;
  }
  function h() {
    var d = P();
    if (_(d))
      return v(d);
    l = setTimeout(h, f(d));
  }
  function v(d) {
    return l = void 0, b && i ? m(d) : (i = s = void 0, r);
  }
  function x() {
    l !== void 0 && clearTimeout(l), p = 0, i = u = s = l = void 0;
  }
  function a() {
    return l === void 0 ? r : v(P());
  }
  function C() {
    var d = P(), y = _(d);
    if (i = arguments, s = this, u = d, y) {
      if (l === void 0)
        return w(u);
      if (c)
        return clearTimeout(l), l = setTimeout(h, t), m(u);
    }
    return l === void 0 && (l = setTimeout(h, t)), r;
  }
  return C.cancel = x, C.flush = a, C;
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
var xe = E, Ce = Symbol.for("react.element"), Ie = Symbol.for("react.fragment"), Se = Object.prototype.hasOwnProperty, Re = xe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Oe = {
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
var I = Y.exports;
const {
  SvelteComponent: Te,
  assign: z,
  binding_callbacks: B,
  check_outros: ke,
  children: Z,
  claim_element: $,
  claim_space: Le,
  component_subscribe: G,
  compute_slots: Pe,
  create_slot: Ae,
  detach: S,
  element: ee,
  empty: H,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Ne,
  get_slot_changes: je,
  group_outros: We,
  init: De,
  insert_hydration: T,
  safe_not_equal: Fe,
  set_custom_element_data: te,
  space: Me,
  transition_in: k,
  transition_out: W,
  update_slot_base: Ue
} = window.__gradio__svelte__internal, {
  beforeUpdate: ze,
  getContext: Be,
  onDestroy: Ge,
  setContext: He
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
        o ? je(
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
      W(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function Ke(e) {
  let t, o, i, s, n = (
    /*$$slots*/
    e[4].default && q(e)
  );
  return {
    c() {
      t = ee("react-portal-target"), o = Me(), n && n.c(), i = H(), this.h();
    },
    l(r) {
      t = $(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), Z(t).forEach(S), o = Le(r), n && n.l(r), i = H(), this.h();
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
      16 && k(n, 1)) : (n = q(r), n.c(), k(n, 1), n.m(i.parentNode, i)) : n && (We(), W(n, 1, 1, () => {
        n = null;
      }), ke());
    },
    i(r) {
      s || (k(n), s = !0);
    },
    o(r) {
      W(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(i)), e[8](null), n && n.d(r);
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
function qe(e, t, o) {
  let i, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Pe(n);
  let {
    svelteInit: u
  } = t;
  const p = O(V(t)), g = O();
  G(e, g, (a) => o(0, i = a));
  const c = O();
  G(e, c, (a) => o(1, s = a));
  const b = [], m = Be("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _
  } = ce() || {}, h = u({
    parent: m,
    props: p,
    target: g,
    slot: c,
    slotKey: w,
    slotIndex: f,
    subSlotIndex: _,
    onDestroy(a) {
      b.push(a);
    }
  });
  He("$$ms-gr-react-wrapper", h), ze(() => {
    p.set(V(t));
  }), Ge(() => {
    b.forEach((a) => a());
  });
  function v(a) {
    B[a ? "unshift" : "push"](() => {
      i = a, g.set(i);
    });
  }
  function x(a) {
    B[a ? "unshift" : "push"](() => {
      s = a, c.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = z(z({}, t), K(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = K(t), [i, s, g, c, l, u, r, n, v, x];
}
class Ve extends Te {
  constructor(t) {
    super(), De(this, t, qe, Ke, Fe, {
      svelteInit: 5
    });
  }
}
const J = window.ms_globals.rerender, A = window.ms_globals.tree;
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
          }, u = r.parent ?? A;
          return u.nodes = [...u.nodes, l], J({
            createPortal: N,
            node: A
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((p) => p.svelteInstance !== s), J({
              createPortal: N,
              node: A
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
    const s = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = D(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(N(E.cloneElement(e._reactElement, {
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
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
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
const X = ne(({
  slot: e,
  clone: t,
  className: o,
  style: i,
  observeAttributes: s
}, n) => {
  const r = re(), [l, u] = oe([]), {
    forceClone: p
  } = ae(), g = p ? !0 : t;
  return se(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function b() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), Ze(n, f), o && f.classList.add(...o.split(" ")), i) {
        const _ = Ye(i);
        Object.keys(_).forEach((h) => {
          f.style[h] = _[h];
        });
      }
    }
    let m = null;
    if (g && window.MutationObserver) {
      let f = function() {
        var x, a, C;
        (x = r.current) != null && x.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: h,
          clonedElement: v
        } = D(e);
        c = v, u(h), c.style.display = "contents", b(), (C = r.current) == null || C.appendChild(c);
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
      c.style.display = "contents", b(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var f, _;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((_ = r.current) == null || _.removeChild(c)), m == null || m.disconnect();
    };
  }, [e, g, o, i, n, s]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
}), et = Je(({
  slots: e,
  children: t,
  ...o
}) => /* @__PURE__ */ I.jsxs(I.Fragment, {
  children: [/* @__PURE__ */ I.jsx("div", {
    style: {
      display: "none"
    },
    children: e.icon || e.src ? t : null
  }), /* @__PURE__ */ I.jsx(ue, {
    ...o,
    icon: e.icon ? /* @__PURE__ */ I.jsx(X, {
      slot: e.icon
    }) : o.icon,
    src: e.src ? /* @__PURE__ */ I.jsx(X, {
      slot: e.src
    }) : o.src || void 0,
    children: e.icon || e.src ? null : t
  })]
}));
export {
  et as Avatar,
  et as default
};
